from rest_framework import serializers
from Employee.models import EmployeeModel


class EmployeeTaskSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = EmployeeModel
        fields = '__all__'  


class EmployeeTaskUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = EmployeeModel
        fields = ['status', 'priority']  

        
