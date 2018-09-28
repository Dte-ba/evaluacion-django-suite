# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-08-20 17:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escuelas', '0071_evento_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='region',
            field=models.IntegerField(choices=[(0, 'Sin definir'), (1, 'Regi\xf3n 1'), (2, 'Regi\xf3n 2'), (3, 'Regi\xf3n 3'), (4, 'Regi\xf3n 4'), (5, 'Regi\xf3n 5'), (6, 'Regi\xf3n 6'), (7, 'Regi\xf3n 7'), (8, 'Regi\xf3n 8'), (9, 'Regi\xf3n 9'), (10, 'Regi\xf3n 10'), (11, 'Regi\xf3n 11'), (12, 'Regi\xf3n 12'), (13, 'Regi\xf3n 13'), (14, 'Regi\xf3n 14'), (15, 'Regi\xf3n 15'), (16, 'Regi\xf3n 16'), (17, 'Regi\xf3n 17'), (18, 'Regi\xf3n 18'), (19, 'Regi\xf3n 19'), (20, 'Regi\xf3n 20'), (21, 'Regi\xf3n 21'), (22, 'Regi\xf3n 22'), (23, 'Regi\xf3n 23'), (24, 'Regi\xf3n 24'), (25, 'Regi\xf3n 25'), (26, 'Regi\xf3n 26'), (27, 'Regi\xf3n 27')], default=0),
        ),
    ]