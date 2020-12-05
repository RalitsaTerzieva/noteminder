from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from accounts.models import UserProfile


class RegisterForm(UserCreationForm):
    pass


class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
