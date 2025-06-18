from rest_framework import serializers
from employees.models import EmployeeModel
from assignments.models import TaskModel


class EmployeeTaskSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = TaskModel
        fields = '__all__'  


class EmployeeTaskUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TaskModel
        fields = ['title','description','status', 'priority','assigned_to','created_by'] 
        read_only_fields = ['created_at', 'updated_at', 'deleted_at'] 

        
