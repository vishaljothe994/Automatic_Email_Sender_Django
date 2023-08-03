from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField() 


class Event(models.Model):
    EVENT_TYPES = (
        ('birthday', 'Birthday'),
        ('work_anniversary', 'Work Anniversary'),
    )
    
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    event_type = models.CharField(max_length=20, choices=EVENT_TYPES)
    event_date = models.DateField()
    
    # def __str__(self):
    #     return f"Event for Employee {self.employee_id}: {self.event_type} on {self.event_date}"
    
   
class EmailTemplate(models.Model):
    event_type = models.CharField(max_length=20, unique=True)
    subject = models.CharField(max_length=200)
    body = models.TextField()
    
    def __str__(self):
        return self.event_type
    

class EmailLog(models.Model):
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    success = models.BooleanField()
    exception_message = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)    