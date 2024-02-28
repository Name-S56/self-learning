import scrapy


class LoginSpider(scrapy.Spider):
    name = "login"
    allowed_domains = ["17k.com"]
    start_urls = ["https://17k.com/........"]

    """重新定义 scrapy原来对于start_urls的处理
    重写start_requests()即可
    """
    # cookie 流程
    # cookie_str = "adasdas=dsda"

    # def start_requests(self):
    #     lst = cookie_str.split(";")
    #     dic = {}
    #     for it in lst:
    #         k,v = it.split("=")
    #         dic[k.strip()] = v.strip()

    #     yield scrapy.Request(
    #         url= self.start_urls[0],
    #         cookies=dic
    #     )

        #登陆流程
    def start_requests(self):
        url = "xxx"
        username = "xxx"
        password = "xxx"

        # yield scrapy.Request(
        # url = "login_url"
        # method = 'post'
        # body=f"loginName={username}&password={password}"
        # callback=self.parse
        # )
        
         #发送post第二方案
        yield scrapy.FormRequest(
            url = url,
            formdata={
                "loginName": username,
                "password":password 
            },
            callback = self.parse
        )
    def parse(self, response):
        yield scrapy.Request(url=LoginSpider.start_requests[0],callback=self.parse_detail)
    def parse_detail(self,resp):
        print(resp.text)


       
