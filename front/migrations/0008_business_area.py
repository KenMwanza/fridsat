# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0007_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='area',
            field=models.CharField(max_length=80, null=True, blank=True),
        ),
    ]
