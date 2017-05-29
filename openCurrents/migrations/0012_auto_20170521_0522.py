# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-21 05:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('openCurrents', '0011_auto_20170428_0832'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=1024)),
                ('date_start', models.DateTimeField(verbose_name='start date')),
                ('date_end', models.DateTimeField(verbose_name='end date')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='date updated')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='date updated')),
            ],
        ),
        migrations.CreateModel(
            name='UserEventRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirmed', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='date updated')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openCurrents.Event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserTimeLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateTimeField(verbose_name='start time')),
                ('date_end', models.DateTimeField(verbose_name='end time')),
                ('verified', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='date updated')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openCurrents.Event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='org',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='date created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='org',
            name='date_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='date updated'),
        ),
        migrations.AddField(
            model_name='orguser',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='date created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orguser',
            name='date_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='date updated'),
        ),
        migrations.AddField(
            model_name='token',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='date created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='token',
            name='date_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='date updated'),
        ),
        migrations.AddField(
            model_name='project',
            name='org',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openCurrents.Org'),
        ),
        migrations.AddField(
            model_name='event',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openCurrents.Project'),
        ),
    ]
