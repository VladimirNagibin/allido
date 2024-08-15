from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

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
        #print(get_image_dimensions(image))
        if image:
            if image.size > 1 * 1024 * 1024:
                raise ValidationError("Размер файла слишком большой ( > 4мб )")
            return image
        else:
            raise ValidationError("Не возможно прочитать файл")
