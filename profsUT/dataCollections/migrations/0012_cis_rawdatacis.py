# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataCollections', '0011_rawdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='CIS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course', models.CharField(max_length=50)),
                ('organization', models.CharField(max_length=50)),
                ('college_school', models.CharField(max_length=50)),
                ('semester', models.CharField(max_length=30)),
                ('forms_distributed', models.IntegerField()),
                ('forms_returned', models.IntegerField()),
                ('instructor_was_num_respondends', models.FloatField()),
                ('instructor_was_average', models.FloatField()),
                ('instructor_was_org_average', models.FloatField()),
                ('instructor_was_college_school_average', models.FloatField()),
                ('instructor_was_uni_average', models.FloatField()),
                ('course_was_num_respondents', models.FloatField()),
                ('course_was_average', models.FloatField()),
                ('course_was_org_average', models.FloatField()),
                ('course_was_college_school_average', models.FloatField()),
                ('course_was_uni_average', models.FloatField()),
                ('instructor', models.ForeignKey(related_name='surveys', to='dataCollections.Instructor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RawDataCIS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField()),
                ('spreadsheet', models.FileField(upload_to=b'', verbose_name=b'XLSX Spreadsheet')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
