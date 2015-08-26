# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0004_business_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='name',
            field=models.CharField(unique=True, max_length=200),
        ),
    ]
