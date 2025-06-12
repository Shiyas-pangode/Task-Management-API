from django.db import models
from Auth.models import CustomUser



class EmployeeModel(models.Model):


    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="tasks_created")  
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="tasks_assigned", null=True, blank=True) 

    def __str__(self):
        return f"{self.created_by} - {self.assigned_to}"
