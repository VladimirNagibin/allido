from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from .models import User
from .forms import RegistrationForm, ProfileForm


class UserCreateView(CreateView):
    form_class = RegistrationForm
    template_name = 'registration/registration_form.html'
    success_url = reverse_lazy('users:edit_profile')


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileForm
    template_name = 'users/user_detail.html'

    def get_object(self):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('users:edit_profile')
