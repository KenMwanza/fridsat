# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0007_auto_20150703_2119'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
    ]
