# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('shuffle_lunch', '0003_shuffle'),
    ]

    operations = [
        migrations.AddField(
            model_name='shuffleevent',
            name='shuffle',
            field=models.ForeignKey(default=1, to='shuffle_lunch.Shuffle'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shuffle',
            name='members',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
    ]
