from django.contrib import admin

from .models import (AstResult, OverUnderResult,
                     WinLossTrend, AtsTrend, OverUnderTrend,
                     Schedule, MatchupStat, EfficiencyStat, SplitStat)


admin.site.register(AstResult)
admin.site.register(OverUnderResult)
admin.site.register(WinLossTrend)
admin.site.register(AtsTrend)
admin.site.register(OverUnderTrend)
admin.site.register(Schedule)
admin.site.register(MatchupStat)
admin.site.register(EfficiencyStat)
admin.site.register(SplitStat)
