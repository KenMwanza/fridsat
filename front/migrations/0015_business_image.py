# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0014_category_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='image',
            field=models.ImageField(null=True, upload_to=b'documents/%Y/%m/%d', blank=True),
        ),
    ]
