# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-13 13:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('opencmis', '0012_auto_20160913_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='baselinevalue',
            name='student',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='opencmis.Student'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='baselinevalue',
            name='week',
            field=models.IntegerField(choices=[(1, 'Week 1'), (2, 'Week 2'), (3, 'Week 3'), (4, 'Week 4'), (5, 'Week 5'), (6, 'Week 6')], default=1),
        ),
    ]
