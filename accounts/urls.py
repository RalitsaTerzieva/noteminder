from django.urls import path, include
from notes.views import ProfileUpdateView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/<pk>/update', ProfileUpdateView.as_view(), name="profile_update"),

]