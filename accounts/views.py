from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from .forms import RegisterForm
from django.views.generic.edit import CreateView, UpdateView
from .models import UserProfile


class SignUpView(CreateView):
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('login')
    form_class = RegisterForm

    def form_valid(self, form):
        # save the user to database
        response = super().form_valid(form)
        # make userprofile of this user
        UserProfile.objects.create(user=self.object)
        return response


@method_decorator(login_required, name='dispatch')
class ProfileDetailView(DetailView):
    model = UserProfile
    template_name = 'accounts/user_profile.html'

    def get_object(self, queryset=None):
        return self.request.user.userprofile


@method_decorator(login_required, name='dispatch')
class ProfileUpdateView(UpdateView):
    model = UserProfile
    fields = ['profile_image']
    template_name = 'accounts/edit_profile.html'
    success_url = reverse_lazy('profile_detail')







