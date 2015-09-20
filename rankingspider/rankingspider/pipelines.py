# -*- coding: utf-8 -*-
import re

from rankingspider.items import TeamItem, ScheduleItem, StatsItem
from rankingspider.mappings import(
    Team, session, Stats, get_team_by_url, get_schedule,
    get_stats
)

from stats.models import Schedule, AstResult, OverUnderTrend
from teams.models import Team

class RankingspiderPipeline(object):

    def _clean_item_data(self, item):
        data = []
        for val in item['data']:
            if val == '--' or not val:
                val = 0

            data += [val]

        item['data'] = data

        return item

    def _save_team_id(self, item):
        team = Team.objects.get(id=item['team'])
        team.team_id = item['data']
        team.save()

    def _save_schedule(self, item):
        check = Schedule.objects.filter(matchup_url=item['data'][2])
        if not check:
            schedule = Schedule(
                team_id=item['team'],
                date=item['data'][0],
                opponent=item['data'][1],
                matchup_url=item['data'][2],
                opponent_url=item['data'][3],
                result=item['data'][4],
                location=item['data'][5],
                wl=item['data'][6],
                conf=item['data'][7]
            )

            if 'Run Line' in item['header']:
                if item['data'][8]:
                    schedule.run_line = item['data'][8]
                if item['data'][9]:
                    schedule.odds = item['data'][9]
                if item['data'][10]:
                    schedule.total = item['data'][10]
                if item['data'][11]:
                    schedule.money = item['data'][11]
            else:
                if item['data'][8]:
                    schedule.spread = item['data'][8]
                if item['data'][9]:
                    schedule.total = item['data'][9]
                if item['data'][10]:
                    schedule.money = item['data'][10]

            print Schedule

            schedule.save()

    def _save_ast_results(self, item):

        check = AstResult.objects.filter(date=item['data'][0], team_id=item['team'])
        if not check:
            ast_result = AstResult(
                team_id=item['team'],
                date=item['data'][0],
                han=item['data'][1],
                opponent=item['data'][2],
                opponent_url=item['data'][3],
                opp_rank=item['data'][4],
            )

            # if 'CHC Line' in item['header'] or 'CLE Line' in item['header']:
            if len(item['data']) >= 8:
                ast_result.chc_line = item['data'][5]
                ast_result.chc_odds = item['data'][6]
                ast_result.result = item['data'][7]
                ast_result.diff = item['data'][8]
            else:
                ast_result.ari_line = item['data'][5]
                ast_result.result = item['data'][6]
                ast_result.diff = item['data'][7]

            ast_result.save()

    def _save_over_under_trends(self, item):
        item = self._clean_item_data(item)

        ou_trend = OverUnderTrend.objects.filter(trend=item['data'][0],
                                                 team_id=item['team'])

        if not ou_trend:
            ou_trend = OverUnderTrend(
                team_id=item['team'],
                trend=item['data'][0],
                over_record=item['data'][1],
                over=item['data'][2],
                uder=item['data'][3],
                total=item['data'][4]
            )
        else:
            ou_trend = ou_trend[0]
            ou_trend.over_record = item['data'][1]
            ou_trend.over = item['data'][2]
            ou_trend.uder = item['data'][3]
            ou_trend.total = item['data'][4]

        ou_trend.save()


    def process_item(self, item, spider):
        if isinstance(item, TeamItem):
            team = Team()
            if not get_team_by_url(item['url'], item['sport']):
                team.url = item['url']
                team.name = item['name']
                team.sport = item['sport']

                session.add(team)
                session.commit()
        elif isinstance(item, ScheduleItem):
            team_id = get_team_by_url(item['team']).id
            schedule = get_schedule(team_id, item['date'])
            if not schedule:
                schedule = Schedule()
                schedule.team = team_id
                schedule.date = item['date']
                schedule.matchup_url = item['matchup_url']
                schedule.location = item['location']
                schedule.opponent = get_team_by_url(item['opponent']).id
            schedule.result = item['result']
            matched = re.match('\w (\d*)-(\d*)', item['result'])
            if matched:
                schedule.status = 'ended'
                schedule.score = int(matched.group(1))
                schedule.opponent_score = int(matched.group(2))
                schedule.score_result = schedule.score-schedule.opponent_score
            else:
                schedule.status = 'not started'
            session.add(schedule)
            session.commit()
        elif isinstance(item, StatsItem):
            if item['stat_type'] == 'team_id':
                self._save_team_id(item)
            elif item['stat_type'] == 'schedule':
                self._save_schedule(item)
            elif item['stat_type'] == 'ast_results':
                self._save_ast_results(item)
            elif item['stat_type'] == 'over_under_trends':
                self._save_over_under_trends(item)
                

        return item
