# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-07-27 19:57
from __future__ import unicode_literals

from django.db import migrations
from escuelas import models

def crear_aplicaciones(apps, schema_editor):
    aplicacion = apps.get_model("escuelas", "Aplicacion")
    aplicacion.objects.get_or_create(nombre=u"SUITE")
    aplicacion.objects.get_or_create(nombre=u"Robótica")

def cargar_app_suite_a_usuarios(apps, schema_editor):
    Perfil = apps.get_model("escuelas", "Perfil")
    Aplicacion = apps.get_model("escuelas", "Aplicacion")

    aplicacion = Aplicacion.objects.get(nombre="SUITE")
    perfiles = Perfil.objects.all()
    for perfil in perfiles:
        perfil.aplicaciones.add(aplicacion)
        perfil.save()


class Migration(migrations.Migration):

    dependencies = [
        ('escuelas', '0057_auto_20180726_2129'),
    ]

    operations = [
        migrations.RunPython(crear_aplicaciones, migrations.RunPython.noop),
        migrations.RunPython(cargar_app_suite_a_usuarios, migrations.RunPython.noop),
    ]
