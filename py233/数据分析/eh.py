import requests
from bs4 import BeautifulSoup
from datetime import datetime
currentDateAndTime = datetime.now()

url="https://e-hentai.org/news.php"
resp = requests.get(url)
resp.encoding="utf-8"

main_page = BeautifulSoup(resp.text,"html.parser")
todayweb = main_page.find("div",attrs={"id":"botm"})
img_src = todayweb.find("img").get("src")
name = currentDateAndTime.day

img_resp = requests.get(img_src)
with open(f"C:/Users/a2950/Pictures/EH/{name}.jpg",mode="wb")as f:
    f.write(img_resp.content)
print("下载完毕")