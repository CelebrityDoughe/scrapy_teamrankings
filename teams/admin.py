# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Team


class TeamAdmin(admin.ModelAdmin):
    search_fields = ('name', )
    list_filter = ('sport', )
    list_display = ('name', 'url', 'sport')

    class Meta:
        model = Team


admin.site.register(Team, TeamAdmin)
