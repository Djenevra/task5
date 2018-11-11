from django.contrib.auth import get_user_model
from rest_framework import serializers
from tasks.models import Task
from billing.models import TaskRelatedNotes
from rest_auth.registration.serializers import RegisterSerializer
from django.utils.translation import gettext as _


User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'user_type', 'balance')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('title', 'description', 'created_by', 'set_price')


class TaskRelatedNotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskRelatedNotes
        fields = ('task', 'executor', 'price')


class RegisterSerializerCustom(RegisterSerializer):
    PURCHASER = 1
    EXECUTOR = 2

    USER_TYPES = (
        (PURCHASER, _('purchaser')),
        (EXECUTOR, _('executor')),
    )

    user_type = serializers.ChoiceField(
        choices=USER_TYPES, required=True, write_only=True)

    def get_cleaned_data(self):
        return {
                'username': self.validated_data.get('username', ''),
                'password1': self.validated_data.get('password1', ''),
                'email': self.validated_data.get('email', ''),
                'user_type': self.validated_data.get('user_type', ''),
            }

    def save(self, request):
        user = super(RegisterSerializerCustom, self).save(request)
        user.user_type = self.cleaned_data.get('user_type')
        user.save()
        return user
