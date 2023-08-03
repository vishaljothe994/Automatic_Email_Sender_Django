from django.urls import path
from .views import SendEventEmails
from email_sender_app import views as api_view

urlpatterns = [
    path('send-email/', api_view.SendEventEmails.as_view(), name='send-email'),
    
]