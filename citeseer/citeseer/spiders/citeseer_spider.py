# -*- coding: utf-8 -*-
"""
Created on Tue May 23 19:59:36 2017

@author: jerry.liu
"""

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from citeseer.items import CiteseerItem


class MySpider(CrawlSpider):
	name = 'citeseer'
	allowed_domains = ['citeseerx.ist.psu.edu']
	start_urls = ['http://citeseerx.ist.psu.edu/search?q=mixed+reality&submit.x=0&submit.y=0&submit=Search&sort=rlv&t=doc']
	rules = (Rule(LinkExtractor(allow=('/viewdoc/')), callback='parse', follow=True),)

	def parse(self, response):
			item = CiteseerItem()
			item['URL'] = response.xpath('//div[@id="result_list"]/div[class="result"]/a/@href').extract()
			item['authors'] = response.xpath('//div[@id="result_list"]/div[class="pubinfo"]/span[@class="authors"]/text()').extract()
			item['pubyear'] = response.xpath('//div[@id="result_list"]/div[class="pubinfo"]/span[@class="pubyear"]/text()').extract_first()
			return item