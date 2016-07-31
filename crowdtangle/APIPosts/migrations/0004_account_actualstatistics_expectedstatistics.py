# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-31 14:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('APIPosts', '0003_auto_20160731_1155'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_id', models.IntegerField()),
                ('name', models.CharField(max_length=250)),
                ('handle', models.CharField(max_length=250)),
                ('profileImage', models.URLField()),
                ('subscriberCount', models.IntegerField()),
                ('url', models.URLField()),
                ('platform', models.CharField(max_length=250)),
                ('verified', models.BooleanField()),
                ('api_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APIPosts.APIData')),
            ],
        ),
        migrations.CreateModel(
            name='ActualStatistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likeCount', models.IntegerField()),
                ('shareCount', models.IntegerField()),
                ('commentCount', models.IntegerField()),
                ('api_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APIPosts.APIData')),
            ],
        ),
        migrations.CreateModel(
            name='ExpectedStatistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likeCount', models.IntegerField()),
                ('shareCount', models.IntegerField()),
                ('commentCount', models.IntegerField()),
                ('api_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APIPosts.APIData')),
            ],
        ),
    ]