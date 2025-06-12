from django.db import models
from django.contrib.auth.models import AbstractUser , Group ,Permission

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('employee', 'Employee'),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='employee')
    groups = models.ManyToManyField(Group, related_name="customuser_groups", blank=True)  
    user_permissions = models.ManyToManyField(Permission, related_name="customuser_permissions", blank=True)

    def __str__(self):
        return self.username
