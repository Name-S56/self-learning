import requests
from bs4 import BeautifulSoup

f = open("新发地菜价.csv",word ="w",encoding="utf-8")

url=""
resp = requests.get(url)

#初始化
page = BeautifulSoup(resp.text,"html.parser")
table = page.find("table",attrs= {"class":""})
trs = table.find_all("tr")[1:]  #除了第一行外的tr
for tr in trs:  #每一行
    tds = tr.find_all("td")
    name = tds[0].text
    xxxx = tds[1].text
    date = tds[2].text
    print(name,xxxx,date)
f.write(f"{name},{xxxx},{date}")
f.close()
resp.close()

