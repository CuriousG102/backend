# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataCollections', '0012_cis_rawdatacis'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cis',
            old_name='instructor_was_num_respondends',
            new_name='instructor_was_num_respondents',
        ),
    ]
