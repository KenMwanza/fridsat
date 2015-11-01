# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0009_custombusinessgroup'),
    ]

    operations = [
        migrations.AddField(
            model_name='custombusinessgroup',
            name='image',
            field=models.ImageField(null=True, upload_to=b'documents/%Y/%m/%d', blank=True),
        ),
    ]
