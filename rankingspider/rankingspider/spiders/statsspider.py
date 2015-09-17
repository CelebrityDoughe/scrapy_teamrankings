# -*- coding: utf-8 -*-
import json
import re

from scrapy.contrib.spiders.crawl import CrawlSpider
from scrapy.http.request import Request
from scrapy.selector import Selector

from bs4 import BeautifulSoup

from rankingspider.items import StatsItem
from rankingspider.mappings import get_all_teams
from rankingspider.utils import strip_rank


class StatsSpider(CrawlSpider):
    name = 'statsspider'
    url = 'https://www.teamrankings.com'

    # map sport url
    sport_url = {'nfl': 'nfl', 'ncf': 'college-footbal',
                         'mlb': 'mlb', 'nba': 'nba', 'ncb': 'ncaa-basketball'}

    def start_requests(self):
        # for schedule
        teams = get_all_teams()
        # for team in teams:
        #     url = '%s/%s/team/%s' % (
        #         self.url, self.sport_url[team.sport], team.url)

        #     request = Request(url, callback=self.schedule)
        #     request.meta['team'] = team.id

        #     yield request

        # for AST Result
        for team in teams:
            url = '%s/%s/team/%s/ats-results' % (
                self.url, self.sport_url[team.sport], team.url)

            request = Request(url, callback=self.ast_results)
            request.meta['team'] = team.id

            yield request

    def schedule(self, response):
        sel = Selector(response)

        # for the schedule
        match_url = []
        table = sel.xpath("//table[@class='tr-table datatable scrollable']")

        headers = table[0].xpath("thead/tr/th/text()").extract()

        if table:
            for tr in table[0].xpath("tbody/tr"):
                item = StatsItem()
                urls = tr.xpath("td/a/@href").extract()
                part_a = tr.xpath("td/a/text()").extract()

                part_b = []

                c = 0
                for td in tr.xpath("td"):

                    # skip for date and name
                    c += 1
                    if c <= 2:
                        continue

                    # if there is no text, append blank
                    text = td.xpath("text()").extract()
                    if not text or text[0] == '--':
                        part_b += ['']
                    else:
                        part_b += text

                match_url += urls[0]

                item['team'] = response.meta['team']
                item['stat_type'] = 'schedule'
                item['data'] = part_a + urls + part_b
                item['header'] = headers

                yield item
    
    def ast_results(self, response):
        sel = Selector(response)

        # for the ast result
        table = sel.xpath("//table[@class='tr-table scrollable datatable no-initial-sort']")

        headers = table[0].xpath("thead/tr/th/text()").extract()

        if table:
            for tr in table[0].xpath("tbody/tr"):
                item = StatsItem()
                data = []
                c = 0
                for td in tr.xpath("td"):
                    # if there is no text, append blank
                    c += 1

                    text = td.xpath("text()").extract()
                    if not text:
                        text = td.xpath("a/text()").extract()
                    if not text:
                        text = td.xpath("strong/text()").extract()

                    if not text or text[0] == '--':
                        text = ['']

                    data += text

                    # 2nd column, add opponent link
                    if c == 3:
                        text = td.xpath("a/@href").extract()
                        if not text:
                            text = ['']
                        data += text

                item['team'] = response.meta['team']
                item['stat_type'] = 'ast_results'
                item['data'] = data
                item['header'] = headers

                yield item

    def OverUnderTrends(self, response):
        sel = Selector(response)

        # for the schedule
        match_url = []
        table = sel.xpath("//table[@class='tr-table datatable scrollable']")

        headers = table[0].xpath("thead/tr/th/text()").extract()

        if table:
            for tr in table[0].xpath("tbody/tr"):
                item = StatsItem()
                urls = tr.xpath("td/a/@href").extract()
                part_a = tr.xpath("td/a/text()").extract()

                part_b = []

                c = 0
                for td in tr.xpath("td"):
                    print td.xpath("text()").extract()

                    # skip for date and name
                    c += 1
                    if c <= 2:
                        continue

                    # if there is no text, append blank
                    text = td.xpath("text()").extract()
                    if not text or text[0] == '--':
                        part_b += ['']
                    else:
                        part_b += text

                match_url += urls[0]

                item['team'] = response.meta['team']
                item['stat_type'] = 'schedule'
                item['data'] = part_a + urls + part_b
                item['header'] = headers

                yield item
    def parse(self, response):
        item = StatsItem()
        print response.url
