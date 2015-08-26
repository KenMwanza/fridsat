# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0003_business_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='website',
            field=models.URLField(null=True, blank=True),
        ),
    ]
