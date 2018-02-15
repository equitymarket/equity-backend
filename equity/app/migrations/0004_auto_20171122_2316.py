# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 15:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_user_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='permission',
            name='name',
            field=models.CharField(default=None, max_length=30, unique=True),
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.Role'),
        ),
    ]
