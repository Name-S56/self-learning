from pyquery import PyQuery
import requests

def get_page_src(url):
    resp = requests.get(url)
    resp.encoding="utf-8"
    return 

def parse_page_src(html):
    doc =PyQuery(html)
    mt_list = doc(".mt-10").items() #class
    for mt in mt_list:
        mt("div > dl:nth-child(1) >dd").eq(0).text()#dl[1] xpath写法第一个dl
        #.eq(0) 筛选完只想要第0个
        #筛选时只要第一个nth-child(1)
        print(mt)
        #同一页面结构
def main():
    url =""

    html = get_page_src(url)
    parse_page_src(html)