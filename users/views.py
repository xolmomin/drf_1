from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.serializers import UserModelSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserModelSerializer
    queryset = User.objects.all()
    filter_backends = (OrderingFilter, DjangoFilterBackend, SearchFilter)
    ordering_fields = ('id', 'username')
    search_fields = ('username', 'email')
    filterset_fields = ('username', 'is_staff')
