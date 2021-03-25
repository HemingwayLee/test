import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class MySpider(CrawlSpider):
    name = 'example'
    allowed_domains = ['ec2-54-238-101-61.ap-northeast-1.compute.amazonaws.com']
    start_urls = ['http://ec2-54-238-101-61.ap-northeast-1.compute.amazonaws.com']

    rules = (
        Rule(LinkExtractor(allow=r'/.*'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print(response)
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)


