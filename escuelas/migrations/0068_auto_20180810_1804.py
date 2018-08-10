# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-08-10 18:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('escuelas', '0067_remove_eventoderobotica_fecha_fin'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeccionDeRobotica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'seccionesDeRobotica',
                'verbose_name_plural': 'Secciones (Robotica)',
            },
        ),
        migrations.AddField(
            model_name='eventoderobotica',
            name='fecha_de_ultima_modificacion',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='eventoderobotica',
            name='seccion',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seccion_eventos_de_robotica', to='escuelas.SeccionDeRobotica'),
        ),
    ]