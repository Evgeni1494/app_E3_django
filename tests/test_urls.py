import pytest
from django.urls import reverse, resolve
from django.test import SimpleTestCase
from django.contrib.auth import views as auth_views
from conversations import views as conversation_views
import uuid

@pytest.mark.django_db
class TestUrls(SimpleTestCase):
    def test_login_url(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func.view_class, auth_views.LoginView)

    def test_home_url(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, conversation_views.home)

    def test_create_conversation_url(self):
        url = reverse('create_conversation')
        self.assertEquals(resolve(url).func, conversation_views.create_conversation)

    def test_conversation_detail_url(self):
        # Génère un UUID valide pour le test
        conversation_id = uuid.uuid4()
        url = reverse('conversation_detail', args=[conversation_id])
        self.assertEquals(resolve(url).func, conversation_views.conversation_detail)
