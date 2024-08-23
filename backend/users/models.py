from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify

from .constants import (ADMIN, MAX_ROLE_LENGTH,
                        MAX_VISIBILITY_IN_GROUP_LENGTH,
                        MODERATOR, ONLY_LOGIN, ROLE_CHOICES, NAME_MAX_LENGHT,
                        VISIBILITY_IN_GROUP_CHOICES, USER)
from core.models import ImageAvatarModel, VisibilityDescriptionModel


class User(AbstractUser, ImageAvatarModel, VisibilityDescriptionModel):
    role = models.CharField(
        max_length=MAX_ROLE_LENGTH,
        choices=ROLE_CHOICES,
        default=USER,
        verbose_name='Роль',
    )
    visibility_in_group = models.CharField(
        max_length=MAX_VISIBILITY_IN_GROUP_LENGTH,
        choices=VISIBILITY_IN_GROUP_CHOICES,
        default=ONLY_LOGIN,
        verbose_name='Видимость в группе',
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


class Community(ImageAvatarModel, VisibilityDescriptionModel):
    name = models.CharField(
        'Название',
        max_length=NAME_MAX_LENGHT,
    )
    slug = models.SlugField(
        'Идентификатор',
        unique=True,
        help_text=(
            'Идентификатор страницы для URL; '
            'разрешены символы латиницы, цифры, дефис и подчёркивание.'
        ),
    )
    date_created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True
    )

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('name',)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(User, self).save(*args, **kwargs)
