

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import status
from rest_framework.exceptions import ValidationError
from .authentication import EmailUsernameModelBackend
from users.models import CustomUser
from django.contrib.auth import authenticate



from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth import authenticate

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    email = serializers.EmailField(required=False)  

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")
        email = attrs.get("email",None)

        user = authenticate(username=username, password=password)

        if not user:
            raise serializers.ValidationError({
                'detail': "Invalid credentials or inactive account"
            })

        if email and user.email.lower() != email.lower():
            raise serializers.ValidationError({"detail": "Email does not match the account"})

        if not user.is_active:
            raise serializers.ValidationError({
                'detail': "User account is inactive"
            })

        # Get default JWT token data (access & refresh)
        data = super().validate(attrs)

        # Add user info to response
        data['user'] = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'role': getattr(user, 'role', None),
        }

        return data

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        token['role'] = getattr(user, 'role', None)
        return token

