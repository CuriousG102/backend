# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataCollections', '0006_auto_20150228_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='uniqueNo',
            field=models.CharField(max_length=10, verbose_name='Course Unique Number'),
            preserve_default=True,
        ),
    ]
