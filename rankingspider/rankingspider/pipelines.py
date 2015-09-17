# -*- coding: utf-8 -*-
import re

from rankingspider.items import TeamItem, ScheduleItem, StatsItem
from rankingspider.mappings import(
    Team, session, Stats, get_team_by_url, get_schedule,
    get_stats
)

from stats.models import Schedule


class RankingspiderPipeline(object):
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
            if item['stat_type'] == 'schedule':

                check = Schedule.objects.filter(matchup_url=item['data'][2])

                if not check:
                    schedule = Schedule(
                        team_id = item['team'],
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

        return item
