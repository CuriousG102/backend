# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataCollections', '0007_auto_20150228_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='profile_photo',
            field=models.ImageField(null=True, upload_to=b'profile_pics'),
            preserve_default=True,
        ),
    ]
