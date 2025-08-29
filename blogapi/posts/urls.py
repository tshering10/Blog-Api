from django.urls import path
from posts.views import PostList, PostDetail
urlpatterns = [
    path('posts/', PostList.as_view(), name="posts"), #list all posts and create new one
    path('posts/<int:pk>/', PostDetail.as_view(), name="post_details"), # update get, delete posts
]
