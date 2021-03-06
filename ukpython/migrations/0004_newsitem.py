# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-27 21:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ukpython', '0003_auto_20170124_1055'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('content_format', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.CharField(max_length=255)),
                ('date', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
