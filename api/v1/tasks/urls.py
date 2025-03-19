from django.urls import path
from .views import TaskCreate , TaskRetrieveUpdateView, TaskAssignView ,TaskDeleteView ,TaskListView

urlpatterns = [
    path('task/', TaskCreate.as_view(), name ='taskcreateapi'), #for task creation
    path('task/tasks/', TaskListView.as_view(), name='task-list'), # for tasks list
    path('task/<int:pk>/', TaskRetrieveUpdateView.as_view(), name='task-detail-update'), #for retrieve by id
    path("task/<int:pk>/assign/", TaskAssignView.as_view(), name="task-assign"),# for task asign
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'), #for tasks delete

]