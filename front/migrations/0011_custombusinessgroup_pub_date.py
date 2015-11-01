# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0010_custombusinessgroup_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='custombusinessgroup',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 1, 22, 56, 26, 318300, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
