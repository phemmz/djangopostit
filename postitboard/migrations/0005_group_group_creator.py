# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-18 14:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('postitboard', '0004_auto_20171017_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='group_creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='group_creator', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
