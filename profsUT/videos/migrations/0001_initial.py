# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataCollections', '0010_auto_20150303_0132'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('video_master', models.FileField(upload_to=b'master_videos')),
                ('video_transcoded', models.BooleanField(default=False)),
                ('video_transcoding', models.BooleanField(default=False)),
                ('transcode_job_id', models.IntegerField(null=True, blank=True)),
                ('video_url', models.URLField(null=True, blank=True)),
                ('video_thumbnail_url', models.URLField(null=True, blank=True)),
                ('instructor', models.ForeignKey(to='dataCollections.Instructor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
