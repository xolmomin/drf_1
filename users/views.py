from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from users.models import User, Product, Category
from users.serializers import UserModelSerializer, ProductModelSerializer, CategoryModelSerializer, \
    ProductListModelSerializer, UserCreateModelSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserModelSerializer
    queryset = User.objects.all()
    filter_backends = (OrderingFilter, DjangoFilterBackend, SearchFilter)
    # ordering_fields = ('id', 'username')
    search_fields = ('username', 'email')

    @action(detail=False, methods=['GET'], url_path='get-me')
    def get_me(self, request, pk=None):
        if request.user.is_authenticated:
            return Response({'message': f'{request.user.username}'})
        return Response({'message': 'login qilinmagan'})

    # filterset_fields = ('username', 'is_staff')
    # http_method_names = ['get', 'post', 'put', 'patch']
    # filter_backends = (DjangoFilterBackend,)
    # filterset_fields = {
    #     'username': ['startswith', 'endswith'],
    #     'email': ['icontains']
    # }


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.filter(is_premium=False)
    serializer_class = ProductListModelSerializer
    filterset_fields = ('category_id',)

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.is_vip:
            return Product.objects.all()
        return super().get_queryset()


class RegisterCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateModelSerializer


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    filter_backends = (DjangoFilterBackend,)
    # filterset_fields = {
    #     'parent': ['exact', 'isnull']
    # }


class ProductRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer


'''
register
JWT


'''


