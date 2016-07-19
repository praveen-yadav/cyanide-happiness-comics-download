# -*- coding: utf-8 -*-

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from CyanideHappiness.items import PicItem
import urlparse

class FirstSpider(CrawlSpider):
    name = "explode"
    allowed_domains = ["explosm.net"]
    start_urls = ['http://www.explosm.net/comics/4361']

    rules = [
    	Rule(LinkExtractor(
    		allow=['/comics/\d\d\d\d']),    	
    		callback='parse_item',
    		follow=True)
    ]
    
    def parse_item(self, response):
    	item = PicItem()
    	image_relative_url = response.xpath('//*[@id="main-comic"]/@src').extract()[0]
    	image_absolute_url = urlparse.urljoin(response.url, image_relative_url.strip())
    	item['image_urls'] = [image_absolute_url]
    	item['title'] = response.xpath('//*[@id="main-comic"]/@src').extract()[0].split('/')[5].split('?')[0]
    	item['url'] = response.xpath('//*[@id="main-comic"]/@src').extract()
    	yield item
