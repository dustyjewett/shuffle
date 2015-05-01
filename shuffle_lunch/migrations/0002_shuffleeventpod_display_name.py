# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shuffle_lunch', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shuffleeventpod',
            name='display_name',
            field=models.CharField(default='Pod 1', max_length=50),
            preserve_default=False,
        ),
    ]
