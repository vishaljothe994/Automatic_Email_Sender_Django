from django.core.mail import send_mail, BadHeaderError
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import Event, EmailTemplate, EmailLog
from django.conf import settings
from django_cron.models import CronJobBase, Schedule
import datetime

class SendEventEmailsCronJob(CronJobBase):
    RUN_EVERY_MINS = 60 * 24  # Run once a day

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'email_sender_app.send_event_emails_cron_job'    # A unique code for this cron job

    def do(self):
        today = datetime.date.today()
        events = Event.objects.filter(event_date=today)

        for event in events:
            try:
                template = EmailTemplate.objects.get(event_type=event.event_type)
                subject = template.subject
                template_name = f'emails/{template.event_type}_email.html'
                context = {'event': event}

                html_message = render_to_string(template_name, context)
                plain_message = strip_tags(html_message)

                try:
                    send_mail(
                        subject,
                        plain_message,
                        settings.EMAIL_HOST_USER,
                        [event.employee.email],
                        html_message=html_message,
                        fail_silently=False
                    )
                    success = True
                    exception_message = None
                except BadHeaderError:
                    success = False
                    exception_message = "Invalid header found in email."
                except Exception as ex:
                    success = False
                    exception_message = str(ex)

                EmailLog.objects.create(
                    event=event,
                    employee=event.employee,
                    success=success,
                    exception_message=exception_message
                )

            except EmailTemplate.DoesNotExist:
                continue