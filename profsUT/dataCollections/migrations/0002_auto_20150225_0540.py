# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataCollections', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='bio',
            field=models.TextField(null=True, verbose_name=b'Short biography of the professor'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='inst_provided_description',
            field=models.TextField(help_text=b'Description for the course provided by the Instructor', null=True, verbose_name=b'Instructor Provided Description'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='reg_provided_description',
            field=models.TextField(help_text=b'Description (text) provided by registrar', null=True, verbose_name=b'Registrar Provided Description'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='syllabus',
            field=models.FileField(null=True, upload_to=b'syllabi'),
            preserve_default=True,
        ),
    ]
