from django.urls import reverse_lazy

from .forms import RegisterForm
from django.views.generic.edit import CreateView

from .models import UserProfile


class SignUpView(CreateView):
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('index')
    form_class = RegisterForm

    def form_valid(self, form):
        response = super().form_valid(form)
        UserProfile.objects.create(user=self.object)
        return response

