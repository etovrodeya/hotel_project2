# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 11:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0008_auto_20170529_1358'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAvatar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='users/', verbose_name='Аватар')),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='avatar',
        ),
        migrations.AddField(
            model_name='useravatar',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
