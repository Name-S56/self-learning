'''
进程1   图片详情页url ,提取图片下载
进程2   下载地址
'''
from urllib import parse#域名操作
from concurrent.futures import ThreadPoolExecutor
import requests
from lxml import etree
from multiprocessing import Process,Queue#队列在此



def   get_img_stc(q):
    url = "http..."
    resp = requests.get(url)
    resp.encoding='utf-8'
    tree=etree.HTML(resp.text)
    fref_list = tree.xpath("//div[@class='']/ul/li/a[1]/@href")
    for href in fref_list:
        href =parse.urljoin(url,href) #拼接url
        #子href 拿到
        child_resp = requests.get(href)
        child_resp = requests.get(url)
        child_resp.encoding='utf-8'
        child_tree = etree.HTML(child_resp.text)
        src = child_tree.xpath("//div[@id='picBody']//img/@src")
        
        q.put(src)
        print(f"{src},被塞进队列")
    src = "完事了"
#进程独立 数据独立 需要中间人
#队列在multiprocessing

from concurrent.futures import ThreadPoolExecutor#线程池
def download(url):
    print("start")
    name = url.split("/")[-1]#熟悉?
    with open(name,"wb") as f:#路径
        resp = requests.get(url)
        f. write(resp.content)
    print("over",url)

def download_img(q):
    with ThreadPoolExecutor(10) as t:
        while 1:
            src = q.get() #获取数据
        #无数据 就会堵塞
            if src =="完事了":
                break
        t.submit(download,src)

if __name__ == '__main__':
    q = Queue()
    p2 = Process(target=get_img_stc,args=(q,))
    p1 = Process(target=download_img,args=(q,))
    p1.start()
    p2.start()