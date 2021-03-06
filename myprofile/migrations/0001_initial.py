# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 19:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(db_index=True, max_length=255, unique=True, verbose_name='Email адрес')),
                ('firstname', models.CharField(blank=True, max_length=100, verbose_name='Имя/Сокращенное название компании')),
                ('surname', models.CharField(blank=True, max_length=150, verbose_name='Фамилия/Полное название компании')),
                ('patronymic', models.CharField(blank=True, max_length=100, verbose_name='Отчество/Название компании на иностранном языке')),
                ('category', models.CharField(choices=[('P', 'Individuals'), ('L', 'Legal person')], default='P', max_length=1, verbose_name='Тип лица')),
                ('status', models.CharField(choices=[('U', 'User'), ('M', 'Manager')], default='U', max_length=1, verbose_name='Статус')),
                ('is_ban', models.BooleanField(default=False, verbose_name='Забанен?')),
                ('balance', models.IntegerField(blank=True, default=0, verbose_name='Баланс')),
                ('country', models.CharField(blank=True, max_length=50, verbose_name='Страна')),
                ('city', models.CharField(blank=True, max_length=50, verbose_name='Город')),
                ('phone', models.CharField(blank=True, max_length=20, verbose_name='Контактный номер')),
                ('index', models.IntegerField(blank=True, verbose_name='Почтовый индекс')),
                ('street', models.CharField(blank=True, max_length=20, verbose_name='Улица')),
                ('home', models.CharField(blank=True, max_length=10, verbose_name='Номер дома')),
                ('region', models.CharField(blank=True, max_length=20, verbose_name='Область')),
                ('office', models.IntegerField(blank=True, verbose_name='Номер дома/офиса')),
                ('birthday', models.DateTimeField(blank=True, verbose_name='День рождения')),
                ('dateofreg', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='user/avatars/', verbose_name='Аватар')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Суперпользователь')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
