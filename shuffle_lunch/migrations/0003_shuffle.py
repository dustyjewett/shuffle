# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shuffle_lunch', '0002_shuffleeventpod_display_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shuffle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('display_name', models.CharField(max_length=200)),
                ('type_description', models.CharField(max_length=20)),
                ('time', models.TimeField()),
                ('firstDate', models.DateTimeField()),
                ('schedule', models.CharField(max_length=20)),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
