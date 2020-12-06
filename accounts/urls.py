from django.urls import path, include
from accounts.views import SignUpView, ProfileDetailView, ProfileUpdateView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/<pk>/update', ProfileUpdateView.as_view(), name="profile_update"),
    path('profile/', ProfileDetailView.as_view(), name="profile_detail"),
    path('register/', SignUpView.as_view(), name="register"),

]