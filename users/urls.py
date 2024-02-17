from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users.views import UserViewSet

router = DefaultRouter()
router.register('users', UserViewSet, basename='user')

urlpatterns = [
    path('api/v1/', include(router.urls))
    # path('users', UserListCreateAPIView.as_view()),
    # path('users', UserCreateAPIView.as_view()),
    # path('users/<pk>', UserRetrieveUpdateDestroyAPIView.as_view()),
    # path('users/<pk>', UserDestroyAPIView.as_view()),
    # path('users/<pk>', UserUpdateAPIView.as_view()),
]
