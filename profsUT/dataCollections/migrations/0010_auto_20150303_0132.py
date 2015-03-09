# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataCollections', '0009_auto_20150303_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='inst_provided_description',
            field=models.TextField(help_text=b'Description for the course provided by the Instructor', null=True, verbose_name=b'Instructor Provided Description', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='reg_provided_description',
            field=models.TextField(help_text=b'Description (text) provided by registrar', null=True, verbose_name=b'Registrar Provided Description', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='syllabus',
            field=models.FileField(null=True, upload_to=b'syllabi', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coursetime',
            name='course',
            field=models.ForeignKey(related_name='times', to='dataCollections.Course'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='instructor',
            name='profile_photo',
            field=models.ImageField(null=True, upload_to=b'profile_pics', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='response',
            name='instructor',
            field=models.ForeignKey(related_name='responses', to='dataCollections.Instructor'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='response',
            name='question',
            field=models.ForeignKey(related_name='responses', to='dataCollections.Question'),
            preserve_default=True,
        ),
    ]
