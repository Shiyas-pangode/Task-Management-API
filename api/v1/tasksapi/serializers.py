
from rest_framework import serializers
from taskapi.models import TaskModel
from taskapi.models import CustomUser  


class TaskCreateSerializer(serializers.ModelSerializer):
    created_by = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all(),  
        required=False  
    )
    assigned_to = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all(),
        allow_null=True, required=False
    )

    class Meta:
        model = TaskModel
        fields = '__all__'


    
class TaskAssignSerializer(serializers.ModelSerializer):
    assigned_to = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.filter(role="employee"),
        required=True
    )

    class Meta:
        model = TaskModel
        fields = ['assigned_to']

    def update(self, instance, validated_data):
        print(f"DEBUG: Validated Data - {validated_data}")  

        assigned_to = Validated_data.get('assigned_to')

        if not assigned_to :
            raise serializers.ValidationError({'assigned_to ': 'This field is required'})

        instance.save()
        return instance

  
class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = TaskModel