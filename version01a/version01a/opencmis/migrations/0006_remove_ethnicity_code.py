# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-07 05:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opencmis', '0005_ethnicity_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ethnicity',
            name='code',
        ),
    ]