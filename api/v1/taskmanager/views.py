from rest_framework import views
from rest_framework.permissions import IsAuthenticated , AllowAny 
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics , status ,permissions
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError


from assignments.models import TaskModel
from . permissions import IsAdminOrManager , IsAdminManagerOrAssignedEmployee ,IsAssignedEmployee ,IsAdminUser
from .serializers import TaskCreateSerializer , TaskAssignSerializer , TaskSerializer

class TaskCreate(generics.CreateAPIView):

    serializer_class= TaskCreateSerializer
    queryset = TaskModel.objects.all()
    permission_classes = [IsAuthenticated ,IsAdminOrManager]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user) 
    
    def create(self, request, *args , **kwargs):
        serializer = self.get_serializer(data=request.data)        
        try:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            
            return Response({
            'status_code':6000,
            'message':'Task  Successfully Created',
            'data':serializer.data
                },status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({
                'status_code':6001,
                'message':'Task retrieve unsuccessfull',
                'errors':serializer.errors
            },status=status.HTTP_400_BAD_REQUEST)
        except Exception as e :
            return Response({
                'status_code ':6001,
                'message':'error occurred during task creation',
                'errors': str(e)
            },status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class TaskListView(generics.ListAPIView):

    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsAdminOrManager]
    def get(self, request, *args , **kwargs):
        
        try:
            queryset = self.filter_queryset(self.get_queryset())
            serializer = self.get_serializer(queryset, many=True)
            
            return Response({
            'status_code':6000,
            'message':'Task retrieved successfully',
            'data':serializer.data
                },status=status.HTTP_200_OK)
        except Exception as e :
            return Response({
                'status_code':6001,
                'message':'Task retrieve unsuccessfull',
                'errors':serializer.errors
            },status=status.HTTP_401_UNAUTHORIZED)


class TaskRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    
    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsAdminManagerOrAssignedEmployee]

    def retrieve(self, request, *args , **kwargs):
        
        try:
            instance=self.get_object()
            serializer = self.get_serializer(instance)
            
            return Response({
            'status_code':6000,
            'message':'Task retrieved successfully',
            'data':serializer.data
                },status=status.HTTP_200_OK)
        except Exception as e :
            return Response({
                'status_code':6001,
                'message':'Task retrieve unsuccessfull',
                'errors':str(e)
            },status=status.HTTP_401_UNAUTHORIZED)



class CustomAPIView(generics.GenericAPIView):
    
    def permission_denied(self, request, message=None, code=None):
        
        response_data = {
            "error": "Access Denied",
            "message": message or "Only Admin and Manager can access this action.",
            "status_code": status.HTTP_403_FORBIDDEN
        }
        raise PermissionDenied(detail=response_data)



class TaskAssignView(CustomAPIView,generics.UpdateAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = TaskAssignSerializer
    permission_classes = [IsAuthenticated, IsAdminOrManager]
    http_method_names = ['patch'] 

    
    def patch(self ,request,*args, **kwargs):
        try :
            instance = self.get_object()
            serializer = self.get_serializer(instance,data=request.data , partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status_code':6000,
                    'message':'assigned',
                    'data':{
                        'id': instance.id,
                        'assigned_to':instance.assigned_to.id
                    }
                },status=status.HTTP_200_OK)
        
            return Response({
                'status_code':6001,
                'message':'Invalid data',
                'errors':serializer.errors
            },status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                'status_code':6002,
                'message':f'Internal error : {str(e)}'
            },status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        


    



class TaskDeleteView(generics.DestroyAPIView):
    queryset = TaskModel.objects.filter(is_deleted=False)
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.soft_delete()
        return Response({
            "status_code":6000,
            "message": "Task deleted successfully.",
            "data": {
                "id":instance.id,
                "title":instance.title,
                "deleted_at":instance.deleted_at
            }
        }, status=status.HTTP_200_OK)

