from django.urls import path
from .views import EmployeeTaskListView, employee_task_detail_update

urlpatterns = [
    path("my-tasks/", EmployeeTaskListView.as_view(), name="employee-tasks"),  
    path("my-tasks/<int:pk>/", employee_task_detail_update, name="employee-task-update"),  
]
