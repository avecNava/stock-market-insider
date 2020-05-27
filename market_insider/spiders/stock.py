
from scrapy import Spider
from scrapy.selector import Selector
from market_insider.items import MarketInsiderItem

class MarketInsiderSpider(Spider):
    name = "market_insider"
    allowed_domains = ["markets.businessinsider.com"]
    start_urls = [
            "https://markets.businessinsider.com/index/components/s&p_500",
            ]

    def parse(self, response):
       
        rows = response.xpath('//*[@id="index-list-container"]/div[2]/table/tr')
        for row in rows:
            yield{
                'name' : row.xpath('td[1]/a/text()').extract(),
                'price':row.xpath('td[2]/text()[1]').extract(),
                'pct':row.xpath('td[5]/span[2]/text()').extract(),
                'datetime':row.xpath('td[7]/span[2]/text()').extract(),
            }
        # for row in rows:
        #     item = InvestmentItem()
        #     item['name'] = row.xpath('td[1]/a/text()').extract()
        #     item['price'] = row.xpath('td[2]/text()[1]').extract()
        #     item['pct'] = row.xpath('td[5]/span[2]/text()').extract()
        #     item['datetime'] = row.xpath('td[7]/span[2]/text()').extract()

        # yield item


# CSS implementation
# table = response.css('div#index-list-container table.table-small') 
# rows = table.css('tr') 

# for row in rows:
# name = row.css("a::text").get()
# high_low = row.css('td:nth-child(2)::text').get()
# date_time = row.css('td:nth-child(7) span:nth-child(2) ::text').get()

# yield {      
#     'name' : name, 
#     'high_low': high_low,
#     'date_time' : date_time                
# }
    

