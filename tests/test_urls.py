import pytest
from django.urls import reverse, resolve
from django.test import SimpleTestCase
from django.contrib.auth import views as auth_views
from conversations import views as conversation_views
import uuid

@pytest.mark.django_db
class TestUrls(SimpleTestCase):
    """
    Test suite for testing the URL configurations of the conversations app.
    """

    def test_login_url(self):
        """
        Test the login URL.
        
        Ensures that the login URL resolves to the correct view class.
        """
        url = reverse('login')
        self.assertEquals(resolve(url).func.view_class, auth_views.LoginView)

    def test_home_url(self):
        """
        Test the home URL.
        
        Ensures that the home URL resolves to the correct view function.
        """
        url = reverse('home')
        self.assertEquals(resolve(url).func, conversation_views.home)

    def test_create_conversation_url(self):
        """
        Test the create conversation URL
        
        Ensures that the create conversation URL resolves to the correct view function.
        """
        url = reverse('create_conversation')
        self.assertEquals(resolve(url).func, conversation_views.create_conversation)

    def test_conversation_detail_url(self):
        """
        Test the conversation detail URL.
        
        Ensures that the conversation detail URL resolves to the correct view function using a valid UUID.
        """
        conversation_id = uuid.uuid4()
        url = reverse('conversation_detail', args=[conversation_id])
        self.assertEquals(resolve(url).func, conversation_views.conversation_detail)
