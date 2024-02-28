import scrapy
from twi_color_ball.items import TwiColorBallItem

class TwiColorsBallSpider(scrapy.Spider):
    name = "twi_colors_ball"
    allowed_domains = ["500.com"]
    start_urls = ["https://datachart.500.com/ssq/"]

    def parse(self, response):
        trs = response.xpath("//tbody[@id='tdata']/tr")#te
        for tr in trs:
            if tr.xpath("./@class").extract_first() == 'tdbck':
                continue
            # red_ball = tr.xpath("./td[@class='chartBall01']/text()").extract()
            #scrapy支持xpath&css混用
            red_ball = tr.css(".chartBall01::text").extract()
            blue_ball = tr.css(".chartBall02::text").extract_first()
            print(red_ball)
            seven = tr.xpath("./td[]")

            cai = TwiColorBallItem()
            cai['seven'] = seven
            cai['red_ball'] = red_ball
            cai['blue_ball'] = blue_ball
            yield cai
        #     dic = {
        #        "red_ball": red_ball,
        #        "blue_ball": blue_ball,
        #        "seven":seven
        #    }
        #     yield dic

"""
存储数据的方案:
1。数据要存储在csv文件中
2。数据存储在mysql数据库中
3.数据存储在mongodb数据库中
4．文件的存储
"""
