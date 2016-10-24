# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-24 22:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('asin', models.CharField(max_length=250)),
                ('genre', models.CharField(max_length=250)),
                ('features', models.CharField(max_length=250)),
                ('images', models.CharField(max_length=250)),
            ],
        ),
    ]
