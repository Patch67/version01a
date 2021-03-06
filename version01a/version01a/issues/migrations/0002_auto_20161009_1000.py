# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-09 09:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='status',
            field=models.CharField(choices=[('O', 'Open'), ('C', 'Closed'), ('H', 'On hold')], default='O', max_length=1),
        ),
        migrations.AlterField(
            model_name='issue',
            name='priority',
            field=models.CharField(choices=[('H', 'High'), ('M', 'Medium'), ('L', 'Low')], default='M', max_length=1),
        ),
        migrations.AlterField(
            model_name='issue',
            name='speed',
            field=models.CharField(choices=[('Q', 'Quick'), ('M', 'Medium'), ('S', 'Slow')], default='M', max_length=1),
        ),
    ]
