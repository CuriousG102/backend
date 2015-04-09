# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataCollections', '0010_auto_20150303_0132'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='video',
            field=models.FileField(null=True, upload_to=b'videos', blank=True),
            preserve_default=True,
        ),
    ]
