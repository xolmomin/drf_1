from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, Serializer


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ('groups', 'user_permissions', 'password', 'date_joined')


class UserDetailModelSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ('groups', 'user_permissions', 'password')
