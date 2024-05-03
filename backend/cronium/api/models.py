from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=40)
    email = models.CharField(max_length=40, unique=True)
    password = models.CharField(max_length=20)

class Project(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
class List(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default=None)
class Task(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    date = models.DateField(default=None)
    time = models.TimeField(default=None)
    flag = models.CharField(max_length=40)
    status = models.CharField(max_length=40)

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True, blank=True)
    list = models.ForeignKey(List, on_delete=models.CASCADE, default=None, null=True, blank=True)