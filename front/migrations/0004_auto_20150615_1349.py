# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0003_county'),
    ]

    operations = [
        migrations.AlterField(
            model_name='county',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='device',
            name='brand',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='device',
            name='category',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
