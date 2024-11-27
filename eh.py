import requests
from bs4 import BeautifulSoup
from datetime import datetime

url="https://e-hentai.org/news.php"
resp = requests.get(url)
resp.encoding="utf-8"
if url:
    print("页面步骤over")
main_page = BeautifulSoup(resp.text,"html.parser")
todayweb = main_page.find("div",attrs={"id":"botm"})
img_src = todayweb.find("img").get("src")

img_resp = requests.get(img_src)
month = datetime.now().strftime("%m")  # 获取当前月份
code = img_src.split("/")[-1]  # 获取图片文件名，格式为 08.webp
name = f"{month}-{code}"  # 拼接成新的文件名，例如 11-08.webp
# 下载图片
img_resp = requests.get(img_src)
with open(f"C:/Users/ASUS/Pictures/eh/{name}", mode="wb") as f:
    f.write(img_resp.content)
print("下载完毕")
# 等待用户输入以结束程序