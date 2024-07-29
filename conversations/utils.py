import os
from openai import OpenAI
from pinecone import Pinecone
import numpy as np
from dotenv import load_dotenv
import uuid
from .models import Conversation, Message

# Configuration Pinecone
load_dotenv()
pc = Pinecone(api_key=os.getenv("PINEKEY"))
index_name = "openai-embed-large"
index = pc.Index(name=index_name)

# Configuration OpenAI
client = OpenAI(api_key=os.getenv("OPENKEY"))

def get_embedding(text, model="text-embedding-3-large"):
    """
    Obtain an embedding vector for the given text using the specified model.

    Args:
        text (str): The text to be embedded.
        model (str): The model to use for embedding (default is "text-embedding-3-large").

    Returns:
        list: The embedding vector.
    """
    text = text.replace("\n", " ")
    response = client.embeddings.create(input=[text], model=model)
    embedding = response.data[0].embedding
    return embedding

def search_in_pinecone(question_embedding, conversation_id):
    """
    Search for results in Pinecone using the question embedding and conversation ID.

    Args:
        question_embedding (list): The embedding of the question.
        conversation_id (str): The ID of the conversation.

    Returns:
        dict: The query results.
    """
    query_results = index.query(
        vector=question_embedding,
        top_k=5,
        namespace=conversation_id,
        include_metadata=True
    )
    return query_results

def search_in_all_namespaces(question_embedding):
    """
    Search for results in all filtered Pinecone namespaces using the question embedding.

    Args:
        question_embedding (list): The embedding of the question.

    Returns:
        list: The final search results.
    """
    stats = index.describe_index_stats()
    namespaces = stats.get("namespaces", {}).keys()
    filtered_namespaces = [ns for ns in namespaces if ns.startswith("SoWePoC")]

    best_namespace = None
    highest_avg_score = -float('inf')
    all_results = []
    all_scores = []
    
    for ns in filtered_namespaces:
        query_results = index.query(
            vector=question_embedding,
            top_k=40,
            namespace=ns,
            include_metadata=True
        )
        results = query_results["matches"]
        scores = [result['score'] for result in results]
        avg_score = np.median(scores)
        all_results.extend(results)
        all_scores.extend([(result['score'], ns, result) for result in results])

        if avg_score > highest_avg_score:
            highest_avg_score = avg_score
            best_namespace = ns

    best_namespace_results = index.query(
        vector=question_embedding,
        top_k=3,
        namespace=best_namespace,
        include_metadata=True
    )
    top_best_namespace_results = sorted(best_namespace_results["matches"], key=lambda x: x["score"], reverse=True)[:3]

    global_high_scores = sorted([score for score in all_scores if score[1] != best_namespace and score[0] >= 0.85], key=lambda x: x[0], reverse=True)[:2]

    final_results = top_best_namespace_results + [x[2] for x in global_high_scores]
    return final_results

def save_question_in_pinecone(question, conversation_id, model="text-embedding-3-large"):
    """
    Save a question in Pinecone with its embedding and metadata.

    Args:
        question (str): The question to save.
        conversation_id (str): The ID of the conversation.
        model (str): The model to use for embedding (default is "text-embedding-3-large").
    """
    question_namespace = f"Q+{conversation_id}"
    embedding = get_embedding(question, model)
    vector_id = str(uuid.uuid4())
    index.upsert(vectors=[(vector_id, embedding, {"text": question})], namespace=question_namespace)
    print(f"Question enregistrée avec metadata dans {question_namespace} avec ID {vector_id}")

def save_interaction_in_pinecone(question, answer, conversation_id, model="text-embedding-3-large"):
    """
    Save an interaction (question and answer) in Pinecone with its embedding and metadata.

    Args:
        question (str): The question of the interaction.
        answer (str): The answer of the interaction.
        conversation_id (str): The ID of the conversation.
        model (str): The model to use for embedding (default is "text-embedding-3-large").
    """
    interaction_text = f"Question: {question} Answer: {answer}"
    embedding = get_embedding(interaction_text, model)
    vector_id = str(uuid.uuid4())
    index.upsert(vectors=[(vector_id, embedding, {"text": interaction_text})], namespace=conversation_id)
    print(f"Interaction enregistrée dans {conversation_id} avec ID {vector_id}")
    save_question_in_pinecone(question, conversation_id, model)

def generate_answer(question, conversation_id):
    """
    Generate an answer to a question using the context from Pinecone and OpenAI.

    Args:
        question (str): The question asked.
        conversation_id (str): The ID of the conversation.

    Returns:
        str: The generated answer.
    """
    question_namespace = f"Q+{conversation_id}"
    question_embedding = get_embedding(question)

    stats = index.describe_index_stats()
    if question_namespace in stats['namespaces']:
        query_results = index.query(
            vector=question_embedding,
            top_k=100,
            namespace=question_namespace,
            include_metadata=True
        )
        all_questions_text = " ".join([result['metadata']['text'] for result in query_results['matches']])
        all_questions_text += " " + question
        question_embedding = get_embedding(all_questions_text)
    
    conversation_query_results = search_in_pinecone(question_embedding, conversation_id)
    context_from_conversation = " ".join([result['metadata']['text'] for result in conversation_query_results['matches']])

    general_query_results = search_in_all_namespaces(question_embedding)
    context_from_general = " ".join([result['metadata']['text'] for result in general_query_results])

    combined_context = f"{context_from_conversation}\n\nDocumentation :{context_from_general}"

    prompt = f"{combined_context}\n\nQuestion: {question}\nRéponse:"
    response = client.chat.completions.create(
        model="gpt-4o",
        seed=17,
        max_tokens=2000,
        top_p=1,
        frequency_penalty=0.2,
        presence_penalty=0.2,
        messages=[
            {"role": "system", "content": "Tu es un assistant pour Sowee et tu parles en français, tu t'adresses à l'agent avec 'vous', tu utilises UNIQUEMENT les données fournies pour répondre aux demandes de l'agent. Tu fais partie d'une application RAG et les données que tu reçois sont composées de toutes les questions de l'utilisateur et des réponses que tu as données, ainsi que d'informations nouvelles par rapport à la question la plus récente. Tes réponses sont détaillées et précises quand la documentation, que tu auras analysée, le permet. Si ta réponse n'est pas trouvée directement dans la documentation, tu DOIS dire à l'agent de reformuler sa question en ajoutant plus de mots-clés faisant partie de sa problématique."},
            {"role": "user", "content": f"{prompt} (si l'information pour répondre à la question ne se trouve pas dans la documentation alors tu dois m'inviter à reformuler ma question en ajoutant plus de mots-clés en rapport avec ma problématique.)"},
        ]
    )
    answer = response.choices[0].message.content
    return answer
