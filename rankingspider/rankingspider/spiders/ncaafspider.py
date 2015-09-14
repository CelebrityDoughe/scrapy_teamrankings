   # -*- coding: utf-8 -*-
import re

from scrapy.contrib.spiders.crawl import CrawlSpider
from scrapy.http.request.form import FormRequest

from bs4 import BeautifulSoup

from rankingspider.items import TeamItem


class NcaafSpider(CrawlSpider):
    name = 'ncaafspider'
    url = 'https://www.teamrankings.com/ajax/league/v3/teams_controller.php'
    data = {'league': 'ncf', 'type': 'chooser', 'view_type': 'teams-chooser'}

    def start_requests(self):
        yield FormRequest(self.url, formdata=self.data)

    def parse(self, response):
        soup = BeautifulSoup(response.body)
        for link in soup.select('a'):
            item = TeamItem()
            item['name'] = link.text.strip()
            item['url'] = re.match('.*/team/(.*)', link['href']).group(1)
            yield item
