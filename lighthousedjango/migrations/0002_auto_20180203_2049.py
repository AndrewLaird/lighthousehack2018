# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-02-03 20:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lighthousedjango', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='black_list',
            field=models.CharField(max_length=1000),
        ),
    ]
