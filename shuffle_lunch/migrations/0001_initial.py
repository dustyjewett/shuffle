# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ShuffleEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('display_name', models.CharField(max_length=200)),
                ('start', models.DateTimeField(verbose_name=b'start time of the event')),
                ('end', models.DateTimeField(verbose_name=b'end time of the event')),
                ('ideal_pod_size', models.IntegerField(default=4)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ShuffleEventPod',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('shuffle_event', models.ForeignKey(to='shuffle_lunch.ShuffleEvent')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ShuffleEventPodConfirmation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comments', models.CharField(max_length=300)),
                ('created_at', models.DateTimeField()),
                ('member', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('pod', models.ForeignKey(to='shuffle_lunch.ShuffleEventPod')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ShuffleEventRSVP',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('response', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField()),
                ('shuffle_event', models.ForeignKey(to='shuffle_lunch.ShuffleEvent')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
