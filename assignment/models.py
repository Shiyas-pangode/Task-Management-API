from django.db import models
from Auth.models import CustomUser  



class TaskModel(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    title = models.CharField(max_length=150)
    description = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="pending") 
    priority = models.CharField(max_length=50, choices=PRIORITY_CHOICES, default="medium")  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="tasks_created_by")  
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="tasks_assigned_by", null=True, blank=True) 

    def __str__(self):
        return f"{self.title} - {self.status}"


class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    subject = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
        




