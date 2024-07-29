import pytest
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from conversations.models import Conversation, Message
import uuid

@pytest.mark.django_db
class TestViews(TestCase):
    """
    Test suite for testing the views of the conversations app.
    """

    def setUp(self):
        """
        Set up the test client, URLs, and create a test user.
        """
        self.client = Client()
        self.login_url = reverse('login')
        self.home_url = reverse('home')
        self.create_conversation_url = reverse('create_conversation')
        self.conversation_id = uuid.uuid4()
        self.conversation_detail_url = reverse('conversation_detail', args=[self.conversation_id])

        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_login_view(self):
        """
        Test the login view.
        
        Ensures that the login page is accessible and uses the correct template.
        """
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_home_view(self):
        """
        Test the home view.
        
        Ensures that the home page is accessible and uses the correct template after login.
        """
        self.client.login(username='testuser', password='12345')
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_create_conversation_view(self):
        """
        Test the create conversation view.
        
        Ensures that a conversation can be created and redirects to the conversation detail page.
        """
        self.client.login(username='testuser', password='12345')
        response = self.client.post(self.create_conversation_url, {'name': 'Test Conversation'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('conversation_detail', args=[Conversation.objects.first().conversation_id]))

    def test_conversation_detail_view(self):
        """
        Test the conversation detail view.
        
        Ensures that the conversation detail page is accessible and uses the correct template.
        """
        conversation = Conversation.objects.create(conversation_id=self.conversation_id, name='Test Conversation')
        response = self.client.get(self.conversation_detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'conversations/conversation_detail.html')
