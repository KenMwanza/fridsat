# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=50)),
                ('county', models.CharField(max_length=20)),
                ('street_address', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=70, blank=True)),
                ('phone_number', models.CharField(max_length=25, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'documents/%Y/%m/%d', blank=True)),
                ('slug', models.SlugField(max_length=1000, null=True, blank=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'businesses',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('slug', models.SlugField(max_length=1000, null=True, blank=True)),
                ('icon', models.CharField(max_length=80, null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=20)),
                ('slug', models.SlugField(max_length=1000, null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'counties',
            },
        ),
    ]
