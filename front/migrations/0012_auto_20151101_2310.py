# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0011_custombusinessgroup_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 1, 23, 10, 28, 780939, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='custombusinessgroup',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 1, 23, 10, 49, 27718, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
