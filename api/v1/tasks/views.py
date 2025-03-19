from rest_framework import views
from rest_framework.permissions import IsAuthenticated , AllowAny
from rest_framework import generics , status ,permissions
from rest_framework.generics import CreateAPIView
from taskapi.models import TaskModel
from . permissions import IsAdminOrManager , IsAdminManagerOrAssignedEmployee ,IsAssignedEmployee ,IsAdminUser
from .serializers import TaskCreateSerializer , TaskAssignSerializer , TaskSerializer

class TaskCreate(generics.CreateAPIView):

    serializer_class= TaskCreateSerializer
    queryset = TaskModel.objects.all()
    permission_classes = [IsAuthenticated ,IsAdminOrManager]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user) 

class TaskListView(generics.ListAPIView):

    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsAdminOrManager]


class TaskRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    
    queryset = TaskModel.objects.all()
    serializer_class = TaskCreateSerializer
    permission_classes = [IsAuthenticated, IsAdminManagerOrAssignedEmployee]


class TaskAssignView(generics.UpdateAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = TaskAssignSerializer
    permission_classes = [IsAuthenticated, IsAdminOrManager]
    http_method_names = ['patch'] 


class TaskDeleteView(generics.DestroyAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]