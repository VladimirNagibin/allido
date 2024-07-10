from django.contrib.auth.models import AbstractUser
from django.db import models

from .constants import (ADMIN, CLOSE, MAX_ROLE_LENGTH,
                        MAX_VISIBILITY_IN_GROUP_LENGTH, MAX_VISIBILITY_LENGTH,
                        MODERATOR, ONLY_LOGIN, ROLE_CHOICES,
                        VISIBILITY_IN_GROUP_CHOICES, VISIBILITY_CHOICES, USER)


class User(AbstractUser):
    description = models.TextField(
        blank=True,
        verbose_name='Обо мне'
    )
    role = models.CharField(
        max_length=MAX_ROLE_LENGTH,
        choices=ROLE_CHOICES,
        default=USER,
        verbose_name='Роль',
    )
    visibility = models.CharField(
        max_length=MAX_VISIBILITY_LENGTH,
        choices=VISIBILITY_CHOICES,
        default=CLOSE,
        verbose_name='Видимость',
    )
    visibility_in_group = models.CharField(
        max_length=MAX_VISIBILITY_IN_GROUP_LENGTH,
        choices=VISIBILITY_IN_GROUP_CHOICES,
        default=ONLY_LOGIN,
        verbose_name='Видимость в группе',
    )
    image = models.ImageField('Картинка', upload_to='users_images', blank=True)
    avatar = models.ImageField(
        'Аватарка',
        upload_to='users_images',
        blank=True,
    )
    slug = models.SlugField(
        'Идентификатор',
        unique=True,
        help_text=(
            'Идентификатор страницы для URL; '
            'разрешены символы латиницы, цифры, дефис и подчёркивание.'
        ),
    )

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('username',)

    def __str__(self):
        return self.username

    @property
    def is_admin(self):
        return self.is_staff or self.is_superuser or self.role == ADMIN

    @property
    def is_moderator(self):
        return self.role == MODERATOR


class Group(models.Model):
    ...