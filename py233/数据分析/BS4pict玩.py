import requests
from bs4 import BeautifulSoup

domain = ""
domain2 = "http://www.umeituku.com/katongdongman/dongmantupian/"
'''
    分两种情况url开头/  
'''
url="http://www.umeituku.com/katongdongman/"
resp= requests.get(url)#主页面,抓取子页面大图
resp.encoding="utf-8"

#bs4
main_page = BeautifulSoup(resp.text,"html.parser")
a_list = main_page.find_all("a",attrs={"class":"TypeBigPics"})

n=1
for a in a_list:
    href = a.get("href")
    child_url= domain + href
    child_resp = requests.get(child_url)
    child_resp.encoding="utf-8"

    child_bs = BeautifulSoup(child_resp.text,"html.parser")
    #找div
    child_bss = child_bs.find("child_bs",attrs={"class":"NewPages"})
    b_list= child_bss.find_all("a")
    for b in b_list:
        b_href = b.get("href")
        b_url =  b_href
        print(b_url)
        b_resp = requests.get(b_url)
        b_resp.encoding="utf-8"
        b_bs = BeautifulSoup(b_resp.text,"html.parser")
        '''
        img_src= div.find("img").get("src")
        name =div.find("img").get("alt")
        img_resp = requests.get(img_src)

    with open(f"pict/{name}.jpg",mode="wb")as f:
        f.write(img_resp.content)
    print("下载完毕")
    n+=1
    #img_resp.content    #字节形式
'''