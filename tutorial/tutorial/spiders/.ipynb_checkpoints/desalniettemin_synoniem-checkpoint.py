import scrapy

class QuoteSpider(scrapy.Spider):
    name = 'desalniettemin'
    start_urls = [
        'https://synoniemen.net/index.php?zoekterm=desalniettemin'
    ]
    
    def parse(self, response):
        synonym_table = response.css("dl.alssynoniemtabel")
        
        all_synonym = synonym_table.css(".nowrap")
        
        syno_desc = synonym_table.css("dd")
        
        for synonym, desc in zip(all_synonym, syno_desc):
            syno = synonym.css("a::text").extract()
            descList = desc.css("a::text").extract()
            
            yield {
                "Synonym": syno,
                "Description": descList
            }
            
            