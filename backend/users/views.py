from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from .models import User
from .forms import RegistrationForm, ProfileForm


class UserCreateView(CreateView):
    form_class = RegistrationForm
    template_name = 'registration/registration_form.html'
    success_url = reverse_lazy('pages:index')


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileForm
    template_name = 'users/edit_profile.html'

    def get_object(self):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy(
            'users:profile',
            kwargs={'username': self.request.user.username}
        )


class UserDetailView(DetailView):
    model = User
    form_class = ProfileForm
    template_name = 'users/profile.html'

    def get_object(self):
        return get_object_or_404(
            User,
            username=self.kwargs['username'],
        )
