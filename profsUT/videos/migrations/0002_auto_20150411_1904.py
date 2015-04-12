# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='instructor',
            field=models.ForeignKey(related_name='video', to='dataCollections.Instructor'),
            preserve_default=True,
        ),
    ]
