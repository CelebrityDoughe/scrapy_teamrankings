# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_auto_20150914_0255'),
        ('stats', '0002_auto_20150916_0606'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='team',
            field=models.ForeignKey(default=1, to='teams.Team'),
            preserve_default=False,
        ),
    ]
