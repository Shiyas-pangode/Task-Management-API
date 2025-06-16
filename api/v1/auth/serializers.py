from django.contrib.auth import authenticate

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import status

from users.models import CustomUser


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    username = serializers.CharField(required=True, )  
    password = serializers.CharField(required=True)
    email = serializers.EmailField(required=False)

    def validate(self, attrs):
        
        username = attrs.get("username") 
        password = attrs.get("password")
        email = attrs.get('email',None)

        user = None

        try:
            user = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError({'detail': 'Invalid credentialsemail'},status=status.HTTP_)

        auth_user = authenticate(username=username, password=password)
        if not auth_user :
            raise ValidationError({'detail':'Invalid credentials'})
                

        if email and auth_user.email != email:
            raise serializers.ValidationError({'detail':'Email does not match'})

        if not user.check_password(password):
            raise serializers.ValidationError({"detail": "Invalid credentials"})

        if not user.is_active:
            raise serializers.ValidationError({"detail": "User account is inactive"})

        data = super().validate(attrs)
        data['role'] = user.role

        return data



