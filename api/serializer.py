from django.contrib.auth import get_user_model
from rest_framework import serializers
from tasks.models import Task
from billing.models import CurrencyCirculation

User = get_user_model()
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email',)

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('title', 'description', 'created_by', 'set_price')

class CurrencyCirculationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyCirculation
        fields = ('user', 'task', 'reason', 'debit', 'credit', 'currency', 'balance')
