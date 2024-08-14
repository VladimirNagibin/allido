from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


User = get_user_model()


class RegistrationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User


class ProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'avatar', 'image',
                  'email', 'visibility', 'visibility_in_group', 'description')
