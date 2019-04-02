import scrapy

class QuotesSpider(scrapy.Spider):

    def start_requests(self):
        urls = [
            'http://swcarpentry.github.io/r-novice-gapminder/reference'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.xpath('//dt/text()').getall()
        for i in page:
            print(i, end=" ")