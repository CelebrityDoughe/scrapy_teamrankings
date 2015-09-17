# -*- coding: utf-8 -*-
import json

from django.db import models
from teams.models import Team
# from schedules.models import Schedule


# class Stats(models.Model):

#     CATEGORY_CHOICES = (
#         ('stats', 'Matchup Stats'),
#         ('efficiency', 'Efficiency Stats'),
#         ('splits', 'Stat Splits'),
#     )

#     schedule = models.ForeignKey(Schedule)
#     category = models.CharField(max_length=32, db_index=True,
#                                 choices=CATEGORY_CHOICES)
#     data = models.TextField()

#     @property
#     def data_json(self):
#         return json.loads(self.data)


# stat for the team page

class AstResult(models.Model):
    date = models.CharField(max_length=10, blank=True)
    han = models.CharField(max_length=10, blank=True)
    opponent = models.CharField(max_length=100, blank=True)
    opponent_url = models.CharField(max_length=100, blank=True)
    opp_rank = models.IntegerField(blank=True, null=True)
    ari_line = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    result = models.CharField(max_length=20, blank=True)
    diff = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)


class OverUnderResult(models.Model):
    date = models.CharField(max_length=10, blank=True)
    han = models.CharField(max_length=10, blank=True)
    opponent = models.CharField(max_length=100, blank=True)
    opponent_url = models.CharField(max_length=100, blank=True)
    opp_rank = models.IntegerField(blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    score = models.CharField(max_length=10, blank=True)
    result = models.CharField(max_length=20, blank=True)
    diff = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)


class WinLossTrend(models.Model):
    trend = models.CharField(max_length=100, blank=True)
    win_loss_record = models.CharField(max_length=10, blank=True)
    win = models.CharField(max_length=10, blank=True)
    mov = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ats = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)


class AtsTrend(models.Model):
    trend = models.CharField(max_length=100, blank=True)
    ats_record = models.CharField(max_length=10, blank=True)
    cover = models.CharField(max_length=10, blank=True)
    mov = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ats = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)


class OverUnderTrend(models.Model):
    trend = models.CharField(max_length=100, blank=True)
    over_record = models.CharField(max_length=10, blank=True)
    over = models.CharField(max_length=10, blank=True)
    uder = models.CharField(max_length=10, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)


class Schedule(models.Model):
    team = models.ForeignKey(Team)
    date = models.CharField(max_length=10, blank=True)
    opponent = models.CharField(max_length=100, blank=True)
    matchup_url = models.URLField()
    opponent_url = models.URLField()
    result = models.CharField(max_length=32)
    location = models.CharField(max_length=16)
    wl = models.CharField(max_length=10, blank=True)
    conf = models.CharField(max_length=10, blank=True)
    spread = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    run_line = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    odd = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total = models.CharField(max_length=10, blank=True)
    money = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)


class MatchupStat(models.Model):
    # stats title that appear at top of table
    schedule = models.ForeignKey(Schedule)
    stat_title = models.CharField(max_length=240)
    team1 = models.CharField(max_length=10)    # n ame of team, column header
    stat_label1 = models.CharField(max_length=30)  # label, first column
    value1 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    rank1 = models.IntegerField(blank=True, null=True)
    team2 = models.CharField(max_length=10)   # name of team, column header
    stat_label2 = models.CharField(max_length=30)  # label, last column
    value2 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    rank2 = models.IntegerField(blank=True, null=True)


class EfficiencyStat(models.Model):
    # stats title that appear at top of table
    schedule = models.ForeignKey(Schedule)
    stat_title = models.CharField(max_length=240)
    stat_label = models.CharField(max_length=30)  # label, first column
    team1 = models.CharField(max_length=10)  # name of team, column header
    value1 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    team2 = models.CharField(max_length=10)    # name of team, column header
    value2 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)


class SplitStat(models.Model):
    # stats title that appear at top of table
    schedule = models.ForeignKey(Schedule)
    stat_title = models.CharField(max_length=240)
    split_stat = models.CharField(max_length=30)  # label, first column
    team1 = models.CharField(max_length=10)  # name of team, column header
    team2 = models.CharField(max_length=10)  # name of team, column header
    season1 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # value of team1 for season
    season2 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    last3games1 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # value of team1 for last3games
    last3games2 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    away_vs_home1 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # value of team1 for away_vs_home
    away_vs_home2 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
