# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0004_auto_20150615_1349'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='county',
            options={'verbose_name_plural': 'counties'},
        ),
        migrations.AlterField(
            model_name='county',
            name='name',
            field=models.CharField(unique=True, max_length=20),
        ),
    ]
