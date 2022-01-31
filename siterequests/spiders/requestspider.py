import scrapy
import json
class APISpider(scrapy.Spider):
    name = 'quotespider'
    start_urls = ['https://quotes.toscrape.com/api/quotes?page=1']

    def parse(self, response):
        jsonObject = json.loads(response.body)

        for quote in jsonObject.get('quotes'):
            yield{
                'author' : quote.get('author').get('name'),
                'quote' : quote.get('text')
            }
        
        if jsonObject.get('has_next') != False:
            yield response.follow('https://quotes.toscrape.com/api/quotes?page='+str(jsonObject.get('page')+1), callback = self.parse)
