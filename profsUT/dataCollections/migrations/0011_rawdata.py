# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataCollections', '0010_auto_20150303_0132'),
    ]

    operations = [
        migrations.CreateModel(
            name='RawData',
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
