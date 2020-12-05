from django.urls import path, include
from notes.views import ProfileUpdateView
from accounts.views import SignUpView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/<pk>/update', ProfileUpdateView.as_view(), name="profile_update"),
    path('register/', SignUpView.as_view(), name="register")

]