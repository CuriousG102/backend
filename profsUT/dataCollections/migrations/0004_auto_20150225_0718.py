# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataCollections', '0003_course_coursename'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coursetime',
            old_name='friday',
            new_name='f',
        ),
        migrations.RenameField(
            model_name='coursetime',
            old_name='monday',
            new_name='m',
        ),
        migrations.RenameField(
            model_name='coursetime',
            old_name='saturday',
            new_name='s',
        ),
        migrations.RenameField(
            model_name='coursetime',
            old_name='sunday',
            new_name='su',
        ),
        migrations.RenameField(
            model_name='coursetime',
            old_name='tuesday',
            new_name='t',
        ),
        migrations.RenameField(
            model_name='coursetime',
            old_name='thursday',
            new_name='th',
        ),
        migrations.RenameField(
            model_name='coursetime',
            old_name='wednesday',
            new_name='w',
        ),
    ]
