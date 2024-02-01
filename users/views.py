from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, CreateAPIView, \
    ListCreateAPIView, RetrieveUpdateDestroyAPIView

from users.serializers import UserModelSerializer, UserDetailModelSerializer


# class UserListAPIView(ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserModelSerializer
#
#
# class UserCreateAPIView(CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserModelSerializer


class UserListCreateAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailModelSerializer


# class UserRetrieveAPIView(RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserDetailModelSerializer
#
#
# class UserDestroyAPIView(DestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserDetailModelSerializer
#
#
# class UserUpdateAPIView(UpdateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserDetailModelSerializer
