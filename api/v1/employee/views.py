from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from taskapi.models import TaskModel
from .serializers import EmployeeTaskSerializer, EmployeeTaskUpdateSerializer
from rest_framework import permissions
from django.shortcuts import get_object_or_404


class EmployeeTaskListView(generics.ListAPIView):
   
    serializer_class = EmployeeTaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return TaskModel.objects.filter(assigned_to=self.request.user).distinct()



class EmployeeTaskUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = EmployeeTaskUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        """Fetch only the task assigned to the logged-in user."""
        task = get_object_or_404(TaskModel, id=self.kwargs["pk"])
        
     
        print(f" DEBUG: Logged-in User -> {self.request.user}")
        print(f" DEBUG: Task ID: {task.id}, Assigned To: {task.assigned_to}")

        
        if task.assigned_to != self.request.user:
            raise PermissionDenied("You are not allowed to update this task.")

        return task
