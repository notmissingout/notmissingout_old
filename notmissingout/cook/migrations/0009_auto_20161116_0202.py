# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-16 02:02
from __future__ import unicode_literals

import cook.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cook', '0008_auto_20161005_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='body',
            field=cook.models.HtmlField(help_text='Body of the recipe, in HTML format.'),
        ),
    ]