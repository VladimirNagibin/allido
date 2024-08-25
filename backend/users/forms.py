from typing import Any
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
# import pprint

from .constants import (HEIGHT_IMAGE_MAX_VALUE, IMAGE_MAX_VALUE,
                        WIDTH_IMAGE_MAX_VALUE)

User = get_user_model()


class RegistrationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User


class ProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'avatar', 'image',
                  'email', 'visibility', 'visibility_in_group', 'description')

    def clean_image(self):
        image = self.cleaned_data.get('image', False)
        if image:
            if image.size > IMAGE_MAX_VALUE:
                raise ValidationError("Размер файла слишком большой")
        return image

    def clean_height_image(self):
        height_image = self.cleaned_data.get('height_image', False)
        if height_image:
            if height_image > HEIGHT_IMAGE_MAX_VALUE:
                raise ValidationError("Высота файла слишком большая")
        return height_image

    def clean_width_image(self):
        width_image = self.cleaned_data.get('width_image', False)
        if width_image:
            if width_image > WIDTH_IMAGE_MAX_VALUE:
                raise ValidationError("Ширина файла слишком большая")
        return width_image
