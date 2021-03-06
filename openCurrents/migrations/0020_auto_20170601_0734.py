# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-06-01 07:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('openCurrents', '0019_auto_20170529_2052'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'get_latest_by': 'datetime_start'},
        ),
        migrations.RemoveField(
            model_name='usertimelog',
            name='project',
        ),
        migrations.AddField(
            model_name='usertimelog',
            name='event',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='openCurrents.Event'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usertimelog',
            name='date_end',
            field=models.DateTimeField(null=True, verbose_name='end time'),
        ),
        migrations.AlterField(
            model_name='usertimelog',
            name='is_verified',
            field=models.BooleanField(default=True),
        ),
    ]
