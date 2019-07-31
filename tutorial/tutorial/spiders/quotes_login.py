import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
from ..items import TutorialItem


class QuoteSpider(scrapy.Spider):
    name = 'quotes_login'
    start_urls = [
        'http://quotes.toscrape.com/login'
    ]
    
    def parse(self, response):
        token = response.css("form input::attr(value)").extract_first()
        return FormRequest.from_response(response, formdata = {
            "csrf_token": token,
            "username": "admin",
            "password": "password"
        }, callback = self.start_scraping)
    
    def start_scraping(self, response):
        open_in_browser(response)
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