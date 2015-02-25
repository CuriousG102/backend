# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataCollections', '0002_auto_20150225_0540'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='courseName',
            field=models.CharField(default='No name', max_length=50),
            preserve_default=False,
        ),
    ]
