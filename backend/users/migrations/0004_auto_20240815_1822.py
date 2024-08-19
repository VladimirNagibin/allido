# Generated by Django 3.2.16 on 2024-08-15 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_community'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='slug',
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('user', 'Пользователь'), ('admin', 'Администратор'), ('moderator', 'Модератор')], default='user', max_length=9, verbose_name='Роль'),
        ),
        migrations.AlterField(
            model_name='user',
            name='visibility',
            field=models.CharField(choices=[('open', 'Открытый'), ('only_login', 'Виден только логин'), ('close', 'Закрытый')], default='close', max_length=10, verbose_name='Видимость'),
        ),
        migrations.AlterField(
            model_name='user',
            name='visibility_in_group',
            field=models.CharField(choices=[('open', 'Открытый'), ('only_login', 'Виден только логин')], default='only_login', max_length=10, verbose_name='Видимость в группе'),
        ),
    ]