# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 10:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_auto_20170528_2116'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Room',
        ),
    ]
