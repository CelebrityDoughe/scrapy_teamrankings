# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_auto_20150914_0255'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='team_id',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
