from rest_framework import serializers
from taskapi.models import TaskModel  


class EmployeeTaskSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = TaskModel
        fields = '__all__'  


class EmployeeTaskUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TaskModel
        fields = ['status', 'priority']  

        
