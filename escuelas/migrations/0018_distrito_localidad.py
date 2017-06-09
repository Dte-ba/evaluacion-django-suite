# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-09 14:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escuelas', '0017_programa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Distrito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'distritos',
                'verbose_name_plural': 'distritos',
            },
        ),
        migrations.CreateModel(
            name='Localidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'localidades',
                'verbose_name_plural': 'localidades',
            },
        ),
    ]
