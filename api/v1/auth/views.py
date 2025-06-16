from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer 
from rest_framework.response import Response
from rest_framework import status

from .serializers import CustomTokenObtainPairSerializer




class UserLoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self , request , *args , **kwargss):
        serializer = self.get_serializer(data=request.data)

        try :
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({
                'status_code':6001,
                'message':'Invalid credentials',
            }, status=status.HTTP_401_UNAUTHORIZED)

        data = serializer.validated_data
        
        return Response({
            'status_code':6000 ,
            'message':'Successfully logged in',
            'data':data
        }, status=status.HTTP_200_OK)
    
  
