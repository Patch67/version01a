# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-13 12:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('opencmis', '0011_auto_20160913_1259'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaselineEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=80)),
                ('blurb', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'BaselineEntries',
            },
        ),
        migrations.CreateModel(
            name='BaselineValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('place', models.CharField(max_length=20)),
                ('date', models.DateTimeField(auto_now=True)),
                ('baseline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opencmis.BaselineEntry')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='BaselineHeadings',
        ),
    ]
