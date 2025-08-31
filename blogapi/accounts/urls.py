from django.urls import path
from accounts.views import RegisterView, MyProfileView, UserProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    
    path('profile/', MyProfileView.as_view(), name="my-profile"),
    path('profile/<int:pk>/', UserProfileView.as_view(), name="user-profile"),
]
