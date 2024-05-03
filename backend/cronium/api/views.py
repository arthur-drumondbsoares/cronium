from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import *
from .mixins import *
from django.shortcuts import get_object_or_404


class BaseView(APIView,HttpMixin):
    """
    Fetch all user information, including single tasks and projects with its lists and tasks
    """
    def get(self, request,user_id):
        #id = int(request.query_params["user_id"])
        user = User.objects.get(pk=user_id)
        
        serializer = UserQuerySerializer(user)
        return Response(serializer.data)
#user/<user_id>/tasks
class UserTasks(APIView, HttpMixin):
    def post(self, request, user_id):
        return self.perform_post(Task, TaskSerializer, request, [User])

class UserPojects(APIView, HttpMixin):
    def post(self, request, user_id):
        return self.perform_post(Project, ProjectSerializer, request, User)

#user/<user_id>
class SingleUser(APIView, HttpMixin):
    def get(self,request,user_id):
        return self.perform_get(User, user_id, UserSerializer, request)
    
    def delete(self, request, user_id):
        return self.perform_delete(User, user_id, request)
            
    def put(self, request, user_id):
        return self.perform_put(User, user_id, UserSerializer, request)
    
#'user/<user_id>/tasks/<task_id>'
class SingleTask(APIView, HttpMixin):
    def put(self, request,task_id):
        return self.perform_put(Task, task_id, TaskSerializer, request)
    

    def delete(self, request, task_id, user_id):
        return self.perform_delete(Task, task_id, request)

#'user/<user_id>/projects/<project_id>'
class SingleProject(APIView, HttpMixin):
    def post(self, request, user_id, project_id):
        if request.headers["Resource"] == 'task':
            return self.perform_post(Task, TaskSerializer, request, [List])

        elif request.headers["Resource"] == 'list':
                return self.perform_post(List, ListSerializer, request, Project)


    def put(self, request, user_id, project_id):
            if request.headers["Resource"] == 'project':
               return self.perform_put(Project, project_id, ProjectSerializer, request)
              
            elif request.headers["Resource"] == 'task':
              task_id = int(request.query_params["task_id"])
              return self.perform_put(Task, task_id, TaskSerializer, request)

            elif request.headers["Resource"] == 'list':
              list_id = int(request.query_params["list_id"])
              return self.perform_put(List, list_id, ListSerializer, request)
    
    def delete(self, request, user_id, project_id):
        if request.headers["Resource"] == 'project':
            return self.perform_delete(Project, project_id, request)


        
        elif request.headers["Resource"] == 'task':
            task_id = int(request.query_params["task_id"])
            return self.perform_delete(Task, task_id, request)


        elif request.headers["Resource"] == 'list':
            list_id = int(request.query_params['list_id'])
            return self.perform_delete(List, list_id, request)



