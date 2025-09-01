from django.shortcuts import render
from accounts.serializers import RegisterSerializer, ProfileSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from .models import Profile
from rest_framework import generics, permissions
from .permissions import IsOwnerOrReadOnlyProfile

# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset =  User.objects.all()
    serializer_class = RegisterSerializer
    
class ProfileListView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class  ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnlyProfile]
    
    
