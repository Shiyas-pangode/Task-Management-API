from rest_framework import generics, permissions , status
from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import UserSerializer
from users.models import CustomUser
from rest_framework.exceptions import ValidationError

class UserRegistrationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]  

    def perform_create(self,serializer):
        serializer.save()

    def post(self,request,*args,**kwargs):

        serializer = self.get_serializer(data=request.data)

        try :
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response({
                'status_code':6000 ,
                'message': 'Successfully registerd',
                'data': serializer.data
            },status=status.HTTP_201_CREATED)
        except ValidationError:
            return Response({
                'status_code':6001,
                'message':'Userregistation failed',
                'errors': serializer.errors
            },status=status.HTTP_400_BAD_REQUEST)
        except Exception as e :
            return Response({
                'status_code': 6002,
                'message':'An unexpected error occurred',
                'errors': str(e)
            },status=status.HTTP_500_INTERNAL_SERVER_ERROR)
