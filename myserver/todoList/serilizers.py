from rest_framework import serializers
from .models import Task


class TaskSErilizer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance