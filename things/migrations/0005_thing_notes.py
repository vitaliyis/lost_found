# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-15 07:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('things', '0004_remove_thing_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='thing',
            name='notes',
            field=models.TextField(blank=True, default=None),
        ),
    ]
