# from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from .models import User
from .forms import RegistrationForm


class UserCreateView(CreateView):
    form_class = RegistrationForm
    template_name = 'registration/registration_form.html'
    success_url = reverse_lazy('pages:index')


class UserDetailViev(DetailView):
    model = User
