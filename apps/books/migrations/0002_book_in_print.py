# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-20 22:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='in_print',
            field=models.BooleanField(default=True, verbose_name=True),
            preserve_default=False,
        ),
    ]