# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 10:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0007_auto_20170529_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='users/', verbose_name='Аватар'),
        ),
    ]