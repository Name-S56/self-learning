import re
import requests

url = "https://movie.douban.com/top250"
headers ={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76"
}
resp = requests.get(url,headers=headers)
pageSource = resp.text

obj = re.compile( r'<span class="title">(?P<name>.*?)</span>.*?<p class="">(?P<direct>.*?)&nbsp;.*?<br>(?P<time>.*?)&nbsp',re.S)
result = obj.finditer(pageSource)
for item in result:
    name =(item.group("name"))
    direct =(item.group("direct"))
    time = (item.group("time"))
    print(name,direct,time)