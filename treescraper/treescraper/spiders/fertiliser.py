# -*- coding: utf-8 -*-
import scrapy


class FertiliserSpider(scrapy.Spider):
    name = 'fertiliser'
    allowed_domains = ['http://swcarpentry.github.io/r-novice-gapminder/reference']
    start_urls = ['http://http://swcarpentry.github.io/r-novice-gapminder/reference/']

    def parse(self, response):
        glossary = response.xpath('//dt/text()').getall()
        yield glossary
