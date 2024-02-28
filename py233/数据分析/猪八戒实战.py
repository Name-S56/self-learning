import requests
from lxml import etree

url= "https://www.zbj.com/fw/?k=saas"
resp = requests.get(url)
resp.encoding="utf-8"
print(resp.text)

#element 工具    数据分布div
#找特定div 目标

#提取数据
et = etree.HTML(resp.text)
divs =et.xpath("//divp[@class='new-service-wrap']/div")

for div in divs:
    price = div.xpath("./div/div/a/div[2]/div[1]/span[1]/text()")
    #//标识子孙后代
    if not price:
        continue
    print(price)
    
'''
r= "_".join(["2","a","c"])
print(r)
'''
