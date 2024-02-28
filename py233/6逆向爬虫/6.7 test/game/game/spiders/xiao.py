import scrapy

class XiaoSpider(scrapy.Spider):
    name = "xiao"       #name
    allowed_domains = ["4399.com"]  #allowed_域名
    start_urls = ["https://www.4399.com/flash/"]   #起始_urls

    def parse(self, response):  #该方法默认处理解析
        #print(response)   #响应对象
        #print(response.text)   #拿到页面原代码
        '''
        #直接提取数据
        #response.json()
        #response.css()
        """
        txt = response.xpath("//ul[@class='n-game cf']/li/a/b/text()").extract() #game name
        print(txt)
        """
        '''
        #分块提取数据
        li_list = response.xpath("//ul[@class='n-game cf']/li")
        for li in li_list:
            name = li.xpath("./a/b/text()").extract_first() 
            categroy = li.xpath("./em/a/text()").extract_first() 
            data = li.xpath("./em/text()").extract_first() 
            dic = {
               "name": name,
               "categroy": categroy,
               "data":data
           }
            yield dic #return 数据.可认为直接(其中经过引擎)给了pipeline
            
