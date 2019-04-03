import scrapy

class FertilizerSpider(scrapy.Spider):
    name = 'Fertilizer'
    start_urls = [
            'http://swcarpentry.github.io/r-novice-gapminder/reference'
    ]
    
    def parse(self, response):
        for keyword in response.xpath('//dt/text()'):
            yield {'keywords': keyword.get()}
