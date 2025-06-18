from rest_framework import generics , status
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied

from employees.models import EmployeeModel
from assignments.models import TaskModel
from .serializers import EmployeeTaskSerializer, EmployeeTaskUpdateSerializer
from functools import partial
from django.shortcuts import get_object_or_404


class EmployeeTaskListView(generics.ListAPIView):
   
    serializer_class = EmployeeTaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return TaskModel.objects.filter(assigned_to=self.request.user).distinct()


@api_view(['GET','PUT','PATCH'])
@permission_classes([IsAuthenticated])
def employee_task_detail_update(request, pk):

    try :
        task =  get_object_or_404(TaskModel ,id=pk)
    except Exception as e :
        return Response({'detail':'Task not found'}, status=status.HTTP_404_NOT_FOUND)

    if task.assigned_to and task.assigned_to != request.user :
        raise PermissionDenied("You are not allowed to access this task.")

    if request.method == 'GET':
        serializer = EmployeeTaskUpdateSerializer(task )
        return Response(serializer.data)
        
    elif request.method == 'PATCH' or request.method == 'PUT' :
        serializer = EmployeeTaskUpdateSerializer(task , data = request.data , partial=partial)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'status_code':6000,
            'message':'Succesfully updated',
            'data':serializer.data
        })
    else:
        return Response({
            'status_code':6001,
            'message':'Update failed',
            'errors':serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)





