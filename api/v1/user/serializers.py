from rest_framework import serializers
from users.models import CustomUser
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'role']
        extra_kwargs = {
            'password': {'write_only': True},  
        }
        

    def create(self, validated_data):
    
        validated_data['password'] = make_password(validated_data['password'])  
        return super().create(validated_data)