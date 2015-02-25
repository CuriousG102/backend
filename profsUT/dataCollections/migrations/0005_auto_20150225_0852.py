# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dataCollections', '0004_auto_20150225_0718'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursetime',
            name='endTime',
            field=models.TimeField(default=datetime.datetime(2015, 2, 25, 8, 52, 23, 514084, tzinfo=utc), verbose_name=b'Course End Time'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='coursetime',
            name='time',
            field=models.TimeField(verbose_name=b'Course Begin Time'),
            preserve_default=True,
        ),
    ]
