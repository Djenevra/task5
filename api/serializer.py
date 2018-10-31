from django.contrib.auth import get_user_model
from rest_framework import serializers
from tasks.models import Task
from billing.models import CurrencyCirculation, TaskRelatedNotes

User = get_user_model()
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'user_type', 'balance')

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('title', 'description', 'created_by', 'set_price')

class CurrencyCirculationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyCirculation
        fields = ('user', 'task', 'reason', 'debit', 'credit', 'currency', 'balance')

class TaskRelatedNotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskRelatedNotes
        fields = ('task', 'executor', 'money')
