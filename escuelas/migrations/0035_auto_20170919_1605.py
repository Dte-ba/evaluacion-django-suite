# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-09-19 16:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escuelas', '0034_evento_acta'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='paquete',
            options={'ordering': ('-fecha_pedido',), 'verbose_name_plural': 'paquetes'},
        ),
    ]