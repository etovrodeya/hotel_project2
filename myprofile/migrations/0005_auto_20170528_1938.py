# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-28 16:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0004_auto_20170227_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='День рождения'),
        ),
    ]
