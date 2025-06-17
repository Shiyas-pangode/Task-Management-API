from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer 
from rest_framework.response import Response
from rest_framework import status , serializers
from .serializers import CustomTokenObtainPairSerializer
from rest_framework.exceptions import APIException


class UserLoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
            data = serializer.validated_data
            return Response(
                {
                    'status_code': 6000,
                    'message': 'Successfully logged in',
                    'data': data,
                },
                status=status.HTTP_200_OK
            )
        except serializers.ValidationError as e:
            return Response(
                {
                    'status_code': 6001,
                    'message': 'Invalid credentials',
                    'errors': e.detail,
                },
                status=status.HTTP_401_UNAUTHORIZED
            )
        except Exception as e:
            return Response(
                {
                    'status_code': 6002,
                    'message': f'An unexpected server error: {e}',
                    'errors': str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        
    
  
