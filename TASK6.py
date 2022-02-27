#Import the libraries
import scrapy

class Sadge(scrapy.Spider):
    name = "Sadge"
    start_urls = ['http://192.168.253.129/algenius/']
    def parse(self, response):
        for x in response.css('img'):
            yield {
                'Image Link': x.xpath('@src').extract_first(),
            }
