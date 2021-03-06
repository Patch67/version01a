# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-12 12:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('opencmis', '0007_student_ethnicity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='status',
            field=models.ForeignKey(default=14, on_delete=django.db.models.deletion.CASCADE, to='opencmis.Status'),
            preserve_default=False,
        ),
    ]
