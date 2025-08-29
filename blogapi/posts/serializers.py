from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"