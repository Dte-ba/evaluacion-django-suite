# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-16 14:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escuelas', '0022_auto_20170609_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='escuela',
            name='email',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='escuela',
            name='telefono',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
