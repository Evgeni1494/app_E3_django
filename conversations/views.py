from django.shortcuts import render, get_object_or_404, redirect
from .models import Conversation, Message
from .forms import MessageForm
from .utils import generate_answer, save_interaction_in_pinecone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required
def home(request):
    """
    Render the home page for authenticated users.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered home page.
    """
    return render(request, 'home.html')

def custom_logout_view(request):
    """
    Log out the user and redirect to the login page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A redirection to the login page.
    """
    logout(request)
    return redirect('login')

def create_conversation(request):
    """
    Create a new conversation.

    If the request method is POST, create a new Conversation object and redirect to the conversation detail page.
    Otherwise, render the conversation creation page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered conversation creation page or a redirection to the conversation detail page.
    """
    if request.method == "POST":
        name = request.POST.get('name')
        conversation = Conversation.objects.create(name=name)
        return redirect('conversation_detail', conversation_id=conversation.conversation_id)
    return render(request, 'conversations/create_conversation.html')

def conversation_detail(request, conversation_id):
    """
    Display the details of a conversation and handle message submission.

    Retrieve the conversation and its messages. If the request method is POST and the form is valid,
    save the user message, generate a bot response, save the interaction in Pinecone, and redirect
    to the conversation detail page. Otherwise, render the conversation detail page with the message form.

    Args:
        request (HttpRequest): The HTTP request object.
        conversation_id (str): The ID of the conversation.

    Returns:
        HttpResponse: The rendered conversation detail page.
    """
    conversation = get_object_or_404(Conversation, conversation_id=conversation_id)
    messages = conversation.messages.all()
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.conversation = conversation
            message.role = 'user'
            message.save()
            answer = generate_answer(message.content, str(conversation.conversation_id))
            Message.objects.create(conversation=conversation, role='bot', content=answer)
            save_interaction_in_pinecone(message.content, answer, str(conversation.conversation_id))
            return redirect('conversation_detail', conversation_id=conversation_id)
    else:
        form = MessageForm()
    return render(request, 'conversations/conversation_detail.html', {'conversation': conversation, 'messages': messages, 'form': form})
