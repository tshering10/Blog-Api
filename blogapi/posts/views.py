from django.shortcuts import render
from posts.serializers import PostSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Post
# Create your views here.

#List and create posts
class PostList(APIView):
    def get(self, request):
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class PostDetail(APIView):
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return None
        
    def get(self, request, pk):
        post = self.get_object(pk)
        if not post:
            return Response({'Error': "Post not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    def put(self, request, pk):
        post = self.get_object(pk)
        if not post:
            return Response({'Error': "Post not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer  = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        post = self.get_object(pk)
        if not post:
            return Response({'Error': "Post not found."}, status=status.HTTP_404_NOT_FOUND)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)