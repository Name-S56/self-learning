"""
    <video> 无直接url,占网速,占内存
    .ts 是视频切片
    名称散列    顺序
    ts文件正确顺序保存 ->M3U -> urf-8 -> M3U8
        1请求M3U8文件
        2加载ts文件
        3正常播放
    服务器压力小,用户体验好

    #EXTM3U
    #EXT-X-TARGETDURATION:13 //视频最大切片时长
    #EXT-X-KEY:METHOD=AES-128,URI="key.key" //切片文件加密方式&密钥地址
                        对称加密
"""

"""F12 XHR  2层M3U8
"""
#拿到视频页的页面源代码
#找到iframe src 为M3U8
#请求到src对应的页面源代码  M3U8地址
#第一层M3U8
#第二层
#ts解密
#对ts 合并
import asyncio
import aiohttp
import aiofiles
import requests
import re
import os
from lxml import etree
from urllib import parse    #拼接
from Crypro.Cipher import AES

def get_page_src(url):
    resp = requests.get(url)
    return resp.text

def get_iframe_src(url):
    page_src = get_page_src(url)
    tree = etree.HTML(page_src)
    src = tree.xpath("//iframe/@src")[0]    #域名
    src_url = parse.urljoin(url,src)    #拼接
    return src_url

def get_1_M3U8(src_url):
    page_src = get_page_src(src_url)
    #re 提取json内容
    obj =re.compile(r'url:"(?P<M3U8_url>.*?)",',re.S)
    result = obj.search(page_src)
    M3U8_url = result.group("M3U8_url")
    return M3U8_url

def get_M3U8(first_M3U8_url):
    #第二层
    first_M3U8 = get_page_src(first_M3U8_url)
    second_m3u8_url = first_M3U8.split()[-1]
    second_m3u8_url = parse.urljoin(first_M3U8_url+second_m3u8_url)

    second_m3u8 = get_page_src(second_m3u8_url)
def download_m3u8(second_m3u8):
    pass

async def download_one(line):
    while 1:#这,就是自省
        try:
            file_name = line.split("/")[-1]
            async with aiohttp.ClientSession() as session:
                async with session.get(line,timeout=30) as resp:#要关 timeout
                    content = await resp.content.read()
                    async with aiofiles.open("","wb") as f:
                        await f.write(content)
            print(line,"下载成功")#2千线程  个别线程下载会失败
        except:
            print("error",line)#都懒得写
            asyncio.sleep((i+1)*5)  #time.sleep()适当的睡眠 异步爬虫没必要

            #前后字符 ? line处理
async def download_all_ts():
    tasks=[]
    with open("2_m3u8.txt","r",encoding="utf-8") as f:
        for line in f:  
            line =line.strip()
            if line.startswith("#"):
                continue    #开头跳过
            task = asyncio.create_task(download_one(line))
            tasks.append(task)
    await asyncio.wait(tasks)


#解密拿key
def get_key():
    #M3U8's 
    key_url=""
    obj = re.compile(r'URI="(?p<key>.*?)"')
    with open ("2_m3u8.txt","r")as f:
        result = obj.search(f.read())
        key_url = result.group("key_url")
        key_str = get_page_src(key_url) #txt
        return key_str.encode('urf-8')
    
#解密
def des_all_ts(key):
    tasks =[]#异步下
    with open("2_m3u8.txt","r") as f:
        for line in f:
            if line.startswith("#"):
                continue
            line = line.strip()
            file_name = line.split("/")[-1]
            #准备异步
            task =asyncio.create_task(des_one(file_name,key))
            key = get_key()
            asyncio.run(des_all_ts(file_name,key))

async def des_one(file,key):
    #AES-128 对称加密...js逆向
    #对称加密  有密钥就能解密
    aes =AES.new(key=key,IV=b"0000000000000000",mode=AES.MODE_CBC) #key mode iv
    async  with aiofiles.open(f"./电影加密后{file}","rb") as f1,\
                    aiofiles.open(f"./电影解密后{file}","rb") as f1:
        content = await f1.read()
        bs = aes.decrypt()
        await f2.write(bs)
    print("文件已经解密",file)

#合并
def merge():
    name_list=[]
    with open("2_m3u8.txt","r") as f:
        for line in f:
            if line.startswith("#"):
                continue
            line = line.strip()
            file_name = line.split("/")[-1]
            #切换工作目录 至"./电影解密后"文件夹
    #1记录当前工作目录
    now_dir= os.getcwd()
    os.chdir("./电影解密后")
    temp= []
    n=1
    for i in range(len(name_list)):
        name = name_list[i]
        temp.append(name)
        if i!=0 and i % 100 ==0:#100个合并一次
            os.system(f"copy /b {names} {n}.ts")
            n+=1
            temp = []#还原新的合并列表
    #循环外剩下的ts
        for i in range(1,1+n):
    #所有操作后  切换回来
            pass
    os.chdir(now_dir)

    os.system()
def main():
    url=""
    src_url = get_iframe_src(url)
    #3访问src_url 提取第一层M3U8
    first_M3U8_url = get_1_M3U8(src_url)
    download_m3u8(first_M3U8_url)

    asyncio.run(download_all_ts())
    # loop = asyncio.get_event_loop() 
    # loop.run_until_complete(download_all_ts())

if __name__ == "__main__":
    asyncio.run(main())