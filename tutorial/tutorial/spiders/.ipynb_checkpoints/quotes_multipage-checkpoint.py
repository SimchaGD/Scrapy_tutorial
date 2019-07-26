import scrapy
from ..items import TutorialItem
class QuoteSpider(scrapy.Spider):
    name = 'quotes_multipage'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]
    
    def parse(self, response):
        # Create instance
        items = TutorialItem()
        
        all_div_quotes = response.css("div.quote")
        
        for quotes in all_div_quotes:
            title = quotes.css("span.text::text").extract()
            author = quotes.css(".author::text").extract()
            tag = quotes.css(".tag::text").extract()
            
            # add data to items container
            items["title"] = title
            items["author"] = author
            items["tag"] = tag
            
            # return items
            yield items
            
            next_page = response.css("li.next a::attr(href)")
            
            if next_page is not None:
                yield response.follow(next_page, callback = self.parse)