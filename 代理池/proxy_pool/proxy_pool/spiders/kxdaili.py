import scrapy
from proxy_pool.items import ProxyPoolItem

class KxdailiSpider(scrapy.Spider):
    name = "kxdaili"
    allowed_domains = []
    start_urls = ["https://www.proxy-list.download/HTTP"]

    def parse(self, response):
        trs = response.xpath('//*[@id="tabli"]/tr')
        for tr in trs:
            ip_address = tr.xpath("./td/text()").extract_first().strip()#/text()
            print(ip_address)
            port = tr.xpath("./td[2]/text()").extract_first().strip()
            print(port)

            node = ProxyPoolItem()
            node['ip_address'] = ip_address
            node['port'] = port
            
            yield node