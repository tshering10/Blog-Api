from django.shortcuts import render
from accounts.serializers import RegisterSerializer, ProfileSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from .models import Profile
from rest_framework import generics, permissions

# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset =  User.objects.all()
    serializer_class = RegisterSerializer
    
#  view /edit own profile
class MyProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        return self.request.user
   
   # view anyone's profile 
class UserProfileView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.AllowAny]