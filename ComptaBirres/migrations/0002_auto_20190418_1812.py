# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-04-18 16:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ComptaBirres', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tirador',
            name='ip',
            field=models.GenericIPAddressField(default='0.0.0.0', null=True, protocol='IPv4'),
        ),
        migrations.AlterField(
            model_name='birra',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 18, 18, 12, 10, 297159)),
        ),
        migrations.AlterField(
            model_name='tirador',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
