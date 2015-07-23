# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0012_business_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='county',
            name='slug',
            field=models.SlugField(max_length=1000, null=True, blank=True),
        ),
    ]
