from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from taskapi.models import CustomUser

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    username = serializers.CharField(required=True, )  # Allow blank usernames
    email = serializers.EmailField(required=True)

    def validate(self, attrs):
        
        username = attrs.get("username") # provide a default value
        email = attrs.get('email')
        password = attrs.get("password")

        user = None

        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError({'detail': 'Invalid credentialsemail'})

        if username:
            auth_user = authenticate(username=username, password=password)
            if auth_user and auth_user.email == email:
                user = auth_user

        if not user.check_password(password):
            raise serializers.ValidationError({"detail": "Invalid credentials"})

        if not user.is_active:
            raise serializers.ValidationError({"detail": "User account is inactive"})

        data = super().validate(attrs)
        data['role'] = user.role

        return data