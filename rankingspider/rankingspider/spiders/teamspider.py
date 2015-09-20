# -*- coding: utf-8 -*-
import re

from scrapy.contrib.spiders.crawl import CrawlSpider
from scrapy.http.request.form import FormRequest

from bs4 import BeautifulSoup

from rankingspider.items import TeamItem


class TeamSpider(CrawlSpider):
    name = 'teamspider'
    url = 'https://www.teamrankings.com/ajax/league/v3/teams_controller.php'
    data = {'type': 'chooser', 'view_type': 'teams-chooser'}
    sports = ('nfl', 'ncf', 'mlb', 'nba', 'ncb')
    #sprots = ('ncb', )

    def start_requests(self):

        for sport in self.sports:
            self.data['league'] = sport
            request = FormRequest(self.url, formdata=self.data)
            request.meta['sport'] = self.data['league']
            yield request

    def parse(self, response):
        soup = BeautifulSoup(response.body, 'lxml')
        for link in soup.select('a'):
            item = TeamItem()
            item['name'] = link.text.strip()
            item['url'] = re.match('.*/team/(.*)', link['href']).group(1)
            item['sport'] = response.meta['sport']
            yield item
