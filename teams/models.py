
# -*- coding: utf-8 -*-
from django.db import models


class Team(models.Model):
    """
    NCAA College Basketball Teams
    """
    url = models.URLField()
    name = models.CharField(max_length=128)
    sport = models.CharField(max_length='10')

    def __unicode__(self):
        return self.name
