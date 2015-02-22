# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('uniqueNo', models.IntegerField(verbose_name='Course Unique Number')),
                ('syllabus', models.FileField(upload_to='syllabi')),
                ('inst_provided_description', models.TextField(verbose_name='Instructor Provided Description', help_text='Description for the course provided by the Instructor')),
                ('reg_provided_description', models.TextField(verbose_name='Registrar Provided Description', help_text='Description (text) provided by registrar')),
                ('semesterSeason', models.CharField(choices=[('FA', 'Fall'), ('SP', 'Spring'), ('SU', 'Summer')], max_length=2)),
                ('semesterYear', models.IntegerField(choices=[(2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015)], max_length=4, default=2015)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CourseTime',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('monday', models.BooleanField(verbose_name='Monday', default=False)),
                ('tuesday', models.BooleanField(verbose_name='Tuesday', default=False)),
                ('wednesday', models.BooleanField(verbose_name='Wednesday', default=False)),
                ('thursday', models.BooleanField(verbose_name='Thursday', default=False)),
                ('friday', models.BooleanField(verbose_name='Friday', default=False)),
                ('saturday', models.BooleanField(verbose_name='Saturday', default=False)),
                ('sunday', models.BooleanField(verbose_name='Sunday', default=False)),
                ('time', models.TimeField(verbose_name='Course Time')),
                ('course', models.ForeignKey(to='dataCollections.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('last', models.CharField(max_length=50)),
                ('first', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('text', models.TextField(verbose_name='Question text')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('text', models.TextField(verbose_name='Response text')),
                ('instructor', models.ForeignKey(to='dataCollections.Instructor')),
                ('question', models.ForeignKey(to='dataCollections.Question')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='course',
            name='instructor',
            field=models.ForeignKey(to='dataCollections.Instructor'),
            preserve_default=True,
        ),
    ]
