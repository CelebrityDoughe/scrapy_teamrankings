# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0003_team_team_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='team_id',
        ),
    ]
