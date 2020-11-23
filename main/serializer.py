from rest_framework import serializers
from .models import *

class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields = ('__all__')


class TaskListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields = ('__all__')

class TaskDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields = ('__all__')


