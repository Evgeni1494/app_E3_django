from django.shortcuts import render, get_object_or_404, redirect
from .models import Conversation, Message
from .forms import MessageForm
from .utils import generate_answer, save_interaction_in_pinecone
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout



@login_required
def home(request):
    return render(request, 'home.html')


def custom_logout_view(request):
    logout(request)
    return redirect('login')


def create_conversation(request):
    if request.method == "POST":
        name = request.POST.get('name')
        conversation = Conversation.objects.create(name=name)
        return redirect('conversation_detail', conversation_id=conversation.conversation_id)
    return render(request, 'conversations/create_conversation.html')

def conversation_detail(request, conversation_id):
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
    # raise ValueError("Intentional for testing logging and alerts")
    return render(request, 'conversations/conversation_detail.html', {'conversation': conversation, 'messages': messages, 'form': form})
