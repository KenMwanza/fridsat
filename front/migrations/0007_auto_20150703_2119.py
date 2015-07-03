# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0006_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=50)),
                ('county', models.CharField(max_length=20)),
                ('street_address', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=70, blank=True)),
                ('phone_number', models.CharField(max_length=25, blank=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Brand',
        ),
        migrations.DeleteModel(
            name='Device',
        ),
    ]
