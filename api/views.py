from django.shortcuts import render#from django.contrib.auth.models import User
from rest_framework import viewsets
from api.serializer import UserSerializer, TaskSerializer, CurrencyCirculationSerializer
from django.contrib.auth import get_user_model
from tasks.models import Task
from billing.models import CurrencyCirculation

User = get_user_model()

class ExecutorViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(user_type = User.EXECUTOR)
    serializer_class = UserSerializer


class PurchaserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(user_type = User.PURCHASER)
    serializer_class = UserSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class CurrencyCirculationViewSet(viewsets.ModelViewSet):
    queryset = CurrencyCirculation.objects.all()
    serializer_class = CurrencyCirculationSerializer
