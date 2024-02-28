#北京新发地
import  requests
from lxml import etree
from concurrent.futures import ThreadPoolExecutor#线程池

f = open("线程池案例.csv","w",encoding="utf-8")

def download (url):
    resp = requests.get(url)
    tree = etree.HTML(resp.text)

    tr_list = tree.xpath("//table[@class='hq_table']/tr")    #[position()>1]
    for tr in tr_list:
        td_texts = tr.xpath("./td/text()")
        s = ",".join(td_texts)
        f.write(s)
        f.write('\n')#方法单页

if __name__ =='__main__':
    with ThreadPoolExecutor(10) as t: #线程池
        for i in range(1,16964):
            url = f"http...{i}.shtml"
            #download(url) 线程池不能这么干
            t.submit(download,url)