from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.views import UserViewSet, ProductListAPIView, ProductRetrieveDestroyAPIView, CategoryListAPIView, \
    RegisterCreateAPIView

router = DefaultRouter()
router.register('users', UserViewSet, basename='user')

urlpatterns = [
    # path('get-token', obtain_auth_token),
    path('1', lambda req: 1/0),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
    path('users/register', RegisterCreateAPIView.as_view(), name='category'),
    path('category', CategoryListAPIView.as_view(), name='category'),
    path('products', ProductListAPIView.as_view(), name='products'),
    path('products/private', ProductListAPIView.as_view(), name='products'),
    path('products/<pk>', ProductRetrieveDestroyAPIView.as_view()),
    # path('users/<pk>', UserRetrieveUpdateDestroyAPIView.as_view()),
    # path('users/<pk>', UserRetrieveUpdateDestroyAPIView.as_view()),
    # path('users/<pk>', UserDestroyAPIView.as_view()),
    # path('users/<pk>', UserUpdateAPIView.as_view()),
]



'''
get-me private

access-token (3min)
refresh-token


{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwODMzOTI5NywiaWF0IjoxNzA4MjUyODk3LCJqdGkiOiJjOGM2MWY3MmQyNTQ0NjgzOWQ0MDc3MDI1NmM0MTEyNCIsInVzZXJfaWQiOjF9.wh_RPCfMobW1Nm2LUAIzZyRSvf3NDqKGfCa-A5k4cVk",
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA4MjUzMTk3LCJpYXQiOjE3MDgyNTI4OTcsImp0aSI6IjgzMGQzZTM1MzVjMDQ3ZmViYmZkMjFmMzVjMzQxMjkwIiwidXNlcl9pZCI6MX0.KJCx6J9cUkd8J1yxiYZ-_bz0nMZdyjVTt4-Gt0-oY7o"
}
'''