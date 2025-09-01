from django.urls import path
from accounts.views import RegisterView, ProfileListView, ProfileDetailView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    
    path('profile/', ProfileListView.as_view(), name="profiles"),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name="profile-details"),
]
