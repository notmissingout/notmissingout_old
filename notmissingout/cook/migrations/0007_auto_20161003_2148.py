# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-03 21:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cook', '0006_auto_20161003_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='secondary_flag',
            field=models.ForeignKey(blank=True, help_text='Optional second flag to display for the location', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='cook.Flag'),
        ),
    ]
