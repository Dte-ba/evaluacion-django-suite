# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-09-03 14:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escuelas', '0073_asignar_numero_de_region_a_eventos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tallerderobotica',
            name='eje',
        ),
        migrations.AddField(
            model_name='tallerderobotica',
            name='ejes',
            field=models.ManyToManyField(blank=True, default=None, null=True, related_name='taller_de_robotica', to='escuelas.EjeDeRobotica'),
        ),
    ]