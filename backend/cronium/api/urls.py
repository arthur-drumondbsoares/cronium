from django.urls import path
from . import views
urlpatterns = [
    path('<user_id>', views.BaseView.as_view()),
    path('user/<user_id>', views.SingleUser.as_view()),
    path('user/<user_id>/tasks', views.UserTasks.as_view()),
    path('user/<user_id>/tasks/<task_id>', views.SingleTask.as_view()),
    path('user/<user_id>/projects', views.UserPojects.as_view()),
    path('user/<user_id>/projects/<project_id>', views.SingleProject.as_view())
]
