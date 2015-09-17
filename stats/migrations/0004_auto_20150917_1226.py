# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_auto_20150914_0255'),
        ('stats', '0003_schedule_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='astresult',
            name='team',
            field=models.ForeignKey(default=1, to='teams.Team'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='atstrend',
            name='team',
            field=models.ForeignKey(default=1, to='teams.Team'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='overunderresult',
            name='team',
            field=models.ForeignKey(default=1, to='teams.Team'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='overundertrend',
            name='team',
            field=models.ForeignKey(default=1, to='teams.Team'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='winlosstrend',
            name='team',
            field=models.ForeignKey(default=1, to='teams.Team'),
            preserve_default=False,
        ),
    ]
