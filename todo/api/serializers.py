from rest_framework import serializers
from todo.models import Todo

class TodoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    completed_status = serializers.BooleanField()

    def create(self, validated_data):
        return Todo.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.completed_status = validated_data.get('completed_status', instance.completed_status)

        instance.save()

        return instance