from django.shortcuts import render#from django.contrib.auth.models import User
from rest_framework import viewsets
from api.serializer import UserSerializer, TaskSerializer
from django.contrib.auth import get_user_model
from tasks.models import Task

User = get_user_model()

class ExecutorViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PurchaserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(user_type = User.PURCHASER)
    serializer_class = UserSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
