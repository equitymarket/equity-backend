# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 09:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20171202_2322'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Stratedy',
            new_name='Strategy',
        ),
        migrations.RenameModel(
            old_name='StratedyClassification',
            new_name='StrategyClassification',
        ),
        migrations.RenameField(
            model_name='buyrecord',
            old_name='stratedy',
            new_name='strategy',
        ),
        migrations.RenameField(
            model_name='strategy',
            old_name='stratedyclassification',
            new_name='strategyclassification',
        ),
        migrations.RenameField(
            model_name='trade',
            old_name='stratedy',
            new_name='strategy',
        ),
    ]