from rest_framework import serializers
from .models import *




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'tasks')
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = '__all__'


class ListQuerySerializer(serializers.ModelSerializer):
    tasks = serializers.SerializerMethodField()
    class Meta:
        model = List
        fields = '__all__'
    def get_tasks(self, obj):
        tasks = obj.task_set.all()
        serializer = TaskSerializer(tasks, many=True)
        return serializer.data
class ProjectQuerySerializer(serializers.ModelSerializer):
    lists = serializers.SerializerMethodField()
    class Meta:
        model = Project
        fields = '__all__'

    def get_lists(self, obj):
        lists = obj.list_set.all()
        serializer = ListQuerySerializer(lists, many=True)
        return serializer.data
    
class UserQuerySerializer(serializers.ModelSerializer):
    tasks = serializers.SerializerMethodField()
    projects = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = '__all__'
    def get_tasks(self, obj):
        tasks = obj.task_set.all()
        serializer = TaskSerializer(tasks, many=True)
        return serializer.data
    def get_projects(self, obj):
        projects = obj.project_set.all()
        serializer = ProjectQuerySerializer(projects, many=True)
        return serializer.data