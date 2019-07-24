import scrapy

class QuoteSpider(scrapy.Spider):
    name = 'synoniem'
    start_urls = [
        'https://synoniemen.net/index.php?zoekterm=desalniettemin'
    ]
    
    def parse(self, response):
                
        all_synonym = response.css(".alssynoniemtabel .nowrap")
        
        syno_desc = response.css(".alssynoniemtabel dd")
        
        for synonym, desc in zip(all_synonym, syno_desc):
            syno = synonym.css("a::text").extract()
            descList = desc.css("a::text").extract()
            
            yield {
                "Synonym": syno,
                "Description": descList
            }
            
            