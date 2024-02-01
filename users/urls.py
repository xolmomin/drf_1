from django.urls import path

from users.views import UserListCreateAPIView, UserRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('users', UserListCreateAPIView.as_view()),
    # path('users', UserCreateAPIView.as_view()),
    path('users/<pk>', UserRetrieveUpdateDestroyAPIView.as_view()),
    # path('users/<pk>', UserDestroyAPIView.as_view()),
    # path('users/<pk>', UserUpdateAPIView.as_view()),
]


'''
blog-list
blog-create
blog-detail/<id>
blog-delete/<id>
blog-update/<id>


/blog 
 - post (201) [blog-create]
 - get  (200) [blog-list]
 

/blog/<id>
 - patch|put (200) [blog-update]
 - get  (200) [blog-detail]
 - delete  (204) [blog-delete]
 

'''