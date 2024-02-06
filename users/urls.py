from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users.views import UserViewSet

router = DefaultRouter()
router.register('users', UserViewSet, basename='user')
# from users.views import UserListCreateAPIView, UserRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', include(router.urls))
    # path('users', UserListCreateAPIView.as_view()),
    # path('users', UserCreateAPIView.as_view()),
    # path('users/<pk>', UserRetrieveUpdateDestroyAPIView.as_view()),
    # path('users/<pk>', UserDestroyAPIView.as_view()),
    # path('users/<pk>', UserUpdateAPIView.as_view()),
]

'''
blog-list
blog-create
blog-detail/<id>
blog-delete/<id> (GET, POST)
blog-update/<id>


/blog 
 - post (201) [blog-create]
 - get  (200) [blog-list]
 

/blog/<id>
 - patch|put (200) [blog-update]
 - get  (200) [blog-detail]
 - delete  (204) [blog-delete]
 
docker
docker compose





'''
