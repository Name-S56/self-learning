import re
import requests

url = "https://movie.douban.com/review/best/"
headers ={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76"
}
resp = requests.get(url,headers=headers)
pageSource = resp.text
obj = re.compile( r'<div data-cid=".*?">.*? <img alt="(?P<name>.*?)" title=.*?<div class="main-bd">.*?<div class="short-content">(?P<value>.*?)&nbsp;',re.S)
result = obj.finditer(pageSource)
for item in result:
    print(item.group("name"))
    #print(item.group("value"))
