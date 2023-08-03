from django.contrib import admin
from .models import Event, EmailTemplate, Employee, EmailLog

admin.site.register(Event)
admin.site.register(EmailTemplate)
admin.site.register(Employee)
admin.site.register(EmailLog)


