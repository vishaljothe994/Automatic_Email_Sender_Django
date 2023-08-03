from django.test import TestCase
from django.urls import reverse
from email_sender_app.models import Employee, Event, EmailTemplate

class SendEventEmailsViewTest(TestCase):
    def setUp(self):
        self.employee = Employee.objects.create(name='John Doe', email='john@example.com')
        self.template = EmailTemplate.objects.create(event_type='birthday', subject='Birthday Email', body='Happy birthday!')
        self.event = Event.objects.create(employee=self.employee, event_type='birthday', event_date='2023-08-04')

    def test_send_event_emails_view(self):
        url = reverse('send-email')  # Adjust the URL name if needed
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Event emails sent successfully')