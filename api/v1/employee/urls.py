from django.urls import path
from .views import EmployeeTaskListView, EmployeeTaskUpdateView

urlpatterns = [
    path("my-tasks/", EmployeeTaskListView.as_view(), name="employee-tasks"),  
    path("my-tasks/<int:pk>/", EmployeeTaskUpdateView.as_view(), name="employee-task-update"),  
]
