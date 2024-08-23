from django.db import models

from users.constants import (CLOSE, MAX_VISIBILITY_LENGTH, VISIBILITY_CHOICES)


class ImageAvatarModel(models.Model):
    height_image = models.PositiveIntegerField(default=0)
    width_image = models.PositiveIntegerField(default=0)
    image = models.ImageField(
        'Картинка',
        upload_to='users_images',
        height_field='height_image',
        width_field='width_image',
        blank=True,
    )
    height_avatar = models.PositiveIntegerField(default=0)
    width_avatar = models.PositiveIntegerField(default=0)
    avatar = models.ImageField(
        'Аватарка',
        upload_to='users_images',
        height_field='height_avatar',
        width_field='width_aratar',
        blank=True,
    )

    class Meta:
        abstract = True


class VisibilityDescriptionModel(models.Model):
    description = models.TextField(
        blank=True,
        verbose_name='Описание'
    )
    visibility = models.CharField(
        max_length=MAX_VISIBILITY_LENGTH,
        choices=VISIBILITY_CHOICES,
        default=CLOSE,
        verbose_name='Видимость',
    )

    class Meta:
        abstract = True
