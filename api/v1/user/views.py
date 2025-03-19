from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import UserSerializer
from taskapi.models import TaskModel
from .permissions import IsManagerOrAdmin

from rest_framework import generics, permissions
from taskapi.models import CustomUser
from .serializers import UserSerializer

class UserRegistrationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]  
