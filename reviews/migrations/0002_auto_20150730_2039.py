# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_comments', '0002_update_user_email_field_length'),
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentwithtitle',
            name='comment_ptr',
        ),
        migrations.DeleteModel(
            name='CommentWithTitle',
        ),
    ]
