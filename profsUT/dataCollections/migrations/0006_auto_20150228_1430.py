# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataCollections', '0005_auto_20150225_0852'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='courseID',
            field=models.CharField(default='NA', max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='inst_provided_description',
            field=models.TextField(help_text='Description for the course provided by the Instructor', null=True, verbose_name='Instructor Provided Description'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='reg_provided_description',
            field=models.TextField(help_text='Description (text) provided by registrar', null=True, verbose_name='Registrar Provided Description'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='syllabus',
            field=models.FileField(upload_to='syllabi', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coursetime',
            name='endTime',
            field=models.TimeField(verbose_name='Course End Time'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coursetime',
            name='time',
            field=models.TimeField(verbose_name='Course Begin Time'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='instructor',
            name='bio',
            field=models.TextField(null=True, verbose_name='Short biography of the professor'),
            preserve_default=True,
        ),
    ]
