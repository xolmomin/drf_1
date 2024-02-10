from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.serializers import UserModelSerializer, UserDetailModelSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserModelSerializer
    queryset = User.objects.all()
    http_method_names = ['get']


#
# class UserListAPIView(ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserModelSerializer
#
#
# # class UserCreateAPIView(CreateAPIView):
# #     queryset = User.objects.all()
# #     serializer_class = UserModelSerializer
#
#
# class UserListCreateAPIView(ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserModelSerializer
#
#     def list(self, request, *args, **kwargs):
#         return super().list(request, *args, **kwargs)
#
#     # def create(self, request, *args, **kwargs):
#     #     serializer = self.get_serializer(data=request.data)
#     #     serializer.is_valid(raise_exception=True)
#     #     self.perform_create(serializer)
#     #     headers = self.get_success_headers(serializer.data)
#     #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
#
#
# # class UserRetrieveUpdateDestroyAPIView(APIView):
# #     def get(self):
# #         pass
# #     def post(self):
# #         pass
# #
# #     def delete(self):
# #         pass
#
# class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserDetailModelSerializer
#
#     def get(self, request, *args, **kwargs):
#         return super().get(request, *args, **kwargs)
#
# # class UserRetrieveAPIView(RetrieveAPIView):
# #     queryset = User.objects.all()
# #     serializer_class = UserDetailModelSerializer
# #
# #
# # class UserDestroyAPIView(DestroyAPIView):
# #     queryset = User.objects.all()
# #     serializer_class = UserDetailModelSerializer
# #
# #
# # class UserUpdateAPIView(UpdateAPIView):
# #     queryset = User.objects.all()
# #     serializer_class = UserDetailModelSerializer
