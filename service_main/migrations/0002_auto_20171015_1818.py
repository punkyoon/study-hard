# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-15 09:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='study',
            name='title',
            field=models.CharField(max_length=80),
        ),
    ]
