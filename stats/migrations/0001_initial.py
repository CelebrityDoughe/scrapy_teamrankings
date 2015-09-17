# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AstResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.CharField(max_length=10, blank=True)),
                ('han', models.CharField(max_length=10, blank=True)),
                ('opponent', models.CharField(max_length=100, blank=True)),
                ('opponent_url', models.CharField(max_length=100, blank=True)),
                ('opp_rank', models.IntegerField(null=True, blank=True)),
                ('ari_line', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('result', models.CharField(max_length=20, blank=True)),
                ('diff', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='AtsTrend',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('trend', models.CharField(max_length=100, blank=True)),
                ('ats_record', models.CharField(max_length=10, blank=True)),
                ('cover', models.CharField(max_length=10, blank=True)),
                ('mov', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('ats', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='EfficiencyStat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stat_title', models.CharField(max_length=240)),
                ('stat_label', models.CharField(max_length=30)),
                ('team1', models.CharField(max_length=10)),
                ('value1', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('team2', models.CharField(max_length=10)),
                ('value2', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='MatchupStat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stat_title', models.CharField(max_length=240)),
                ('team1', models.CharField(max_length=10)),
                ('stat_label1', models.CharField(max_length=30)),
                ('value1', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('rank1', models.IntegerField(null=True, blank=True)),
                ('team2', models.CharField(max_length=10)),
                ('stat_label2', models.CharField(max_length=30)),
                ('value2', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('rank2', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='OverUnderResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.CharField(max_length=10, blank=True)),
                ('han', models.CharField(max_length=10, blank=True)),
                ('opponent', models.CharField(max_length=100, blank=True)),
                ('opponent_url', models.CharField(max_length=100, blank=True)),
                ('opp_rank', models.IntegerField(null=True, blank=True)),
                ('total', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('score', models.CharField(max_length=10, blank=True)),
                ('result', models.CharField(max_length=20, blank=True)),
                ('diff', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='OverUnderTrend',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('trend', models.CharField(max_length=100, blank=True)),
                ('over_record', models.CharField(max_length=10, blank=True)),
                ('over', models.CharField(max_length=10, blank=True)),
                ('uder', models.CharField(max_length=10, blank=True)),
                ('total', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.CharField(max_length=10, blank=True)),
                ('opponent', models.CharField(max_length=100, blank=True)),
                ('opponent_url', models.URLField()),
                ('matchup_url', models.URLField()),
                ('result', models.CharField(max_length=32)),
                ('location', models.CharField(max_length=16)),
                ('wl', models.CharField(max_length=10, blank=True)),
                ('conf', models.CharField(max_length=10, blank=True)),
                ('total', models.CharField(max_length=10, blank=True)),
                ('spread', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='SplitStat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stat_title', models.CharField(max_length=240)),
                ('split_stat', models.CharField(max_length=30)),
                ('team1', models.CharField(max_length=10)),
                ('team2', models.CharField(max_length=10)),
                ('season1', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('season2', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('last3games1', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('last3games2', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('away_vs_home1', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('away_vs_home2', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('schedule', models.ForeignKey(to='stats.Schedule')),
            ],
        ),
        migrations.CreateModel(
            name='WinLossTrend',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('trend', models.CharField(max_length=100, blank=True)),
                ('win_loss_record', models.CharField(max_length=10, blank=True)),
                ('win', models.CharField(max_length=10, blank=True)),
                ('mov', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('ats', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='matchupstat',
            name='schedule',
            field=models.ForeignKey(to='stats.Schedule'),
        ),
        migrations.AddField(
            model_name='efficiencystat',
            name='schedule',
            field=models.ForeignKey(to='stats.Schedule'),
        ),
    ]
