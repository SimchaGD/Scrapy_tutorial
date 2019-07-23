import scrapy

class QuoteSpider(scrapy.Spider):
    name = 'hello'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]
    
    def parse(self, response):
        title = response.css('title::text').extract()
        
        yield {'titletext': title}