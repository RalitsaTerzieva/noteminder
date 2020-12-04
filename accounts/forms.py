from django.contrib.auth.models import User
from django.forms import ModelForm
from accounts.models import UserProfile


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
