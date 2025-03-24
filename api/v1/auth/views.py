from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer 
from .serializers import CustomTokenObtainPairSerializer
from rest_framework import serializers



class UserLoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    
  
