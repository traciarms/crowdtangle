# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-31 15:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('APIPosts', '0004_account_actualstatistics_expectedstatistics'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expectedstatistics',
            name='api_data',
        ),
        migrations.AddField(
            model_name='apidata',
            name='exp_statistics',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='APIPosts.ExpectedStatistics'),
        ),
    ]
