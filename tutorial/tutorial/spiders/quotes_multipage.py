import scrapy
from ..items import TutorialItem
class QuoteSpider(scrapy.Spider):
    name = 'quotes_multipage'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]
    next_page_nr = 2
    
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
            
            next_page = 'http://quotes.toscrape.com/{}/'.format(QuoteSpider.next_page_nr)
            
            if QuoteSpider.next_page_nr < 11:
                QuoteSpider.next_page_nr += 1
                yield response.follow(next_page, callback = self.parse)