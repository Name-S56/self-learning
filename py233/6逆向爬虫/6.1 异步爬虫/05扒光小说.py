import asyncio
import aiofiles
import aiohttp
import requests
from lxml import etree
import os
import time
#看页面源代码 

def mkdir(path):
	folder = os.path.exists(path)
	if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹
		os.makedirs(path)            #makedirs 创建文件时如果路径不存在会创建这个路径
 

def get_every_chapter_url(url):
     headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        }
     resp = requests.get(url,headers=headers,verify=False)#resp.text
     tree = etree.HTML(resp.text)
     href_list =tree.xpath("//div[@class='book_list']/span/a/@href")   #href
     return href_list


async def download_one(url):
    while 1:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as resp:
                    page_sources = await resp.text()
                    tree = etree.HTML(page_sources)
                    title = tree.xpath("//div[@class ='']/h1/text()")[0].strip()
                    content = tree.xpath("").replace("\u3000"," ")

                    async with aiofiles.open(f"./xx/{title}.txt","w") as f:
                        f.write(content)
                    break
        except:
            print("try",url)

async def download(href_list):
    tasks=[]
    for href in href_list:
        t = asyncio.create_task(download_one(href))#单独下载任务
        tasks.append(t)
    await asyncio.wait(tasks)

def main():
    #拿到每一个章节url
    url =" "
    
    href_list =get_every_chapter_url(url)
    #启动协程,开始一节一节下载
    asyncio.run(download(href_list))
    """
    tasks =[]
    for href in href_list:
    t = asyncio.create_task()移到download
    """


if __name__ == "__main__":
    asyncio.run(main())