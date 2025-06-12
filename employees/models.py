from django.db import models
from users.models import CustomUser
from general.models import BaseModel
from assignments.models import TaskModel


class EmployeeModel(BaseModel):

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

    title = models.CharField(max_length=150 )
    description = models.TextField(default='')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="pending") 
    priority = models.CharField(max_length=50, choices=PRIORITY_CHOICES, default="medium")

    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="tasks_created")  
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="tasks_assigned",default='' ) 

    def __str__(self):
        return f"{self.assigned_to} - {self.priority}"
