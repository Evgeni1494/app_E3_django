from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_conversation, name='create_conversation'),
    path('<uuid:conversation_id>/', views.conversation_detail, name='conversation_detail'),
]

