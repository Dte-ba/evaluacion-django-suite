# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-08-15 13:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escuelas', '0018_perfil_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='escuela',
            name='estado',
            field=models.BooleanField(default=True),
        ),
    ]