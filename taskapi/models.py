from django.db import models
from django.contrib.auth.models import AbstractUser , Group ,Permission

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('employee', 'Employee'),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='employee')
    groups = models.ManyToManyField(Group, related_name="customuser_groups", blank=True)  # ✅ FIXED
    user_permissions = models.ManyToManyField(Permission, related_name="customuser_permissions", blank=True)  # ✅ FIXED

    
    def __str__(self):
        return self.username

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

    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="tasks_created")  
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="tasks_assigned", null=True, blank=True) 

    def __str__(self):
        return f"{self.title} - {self.status}"
