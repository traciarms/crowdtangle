# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-31 03:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='APIData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_id', models.IntegerField()),
                ('platform', models.CharField(max_length=250)),
                ('date', models.DateTimeField()),
                ('type', models.CharField(max_length=250)),
                ('message', models.CharField(max_length=250)),
                ('expandedLinks', models.CharField(max_length=250)),
                ('link', models.CharField(max_length=250)),
                ('postUrl', models.CharField(max_length=250)),
                ('subscriberCount', models.IntegerField()),
                ('score', models.DecimalField(decimal_places=12, max_digits=20)),
            ],
        ),
    ]