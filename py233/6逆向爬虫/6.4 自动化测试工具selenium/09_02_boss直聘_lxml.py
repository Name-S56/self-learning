#用selenium+lxml 完成数据抓取
from selenium.webdriver import Firefox
from selenium.webdriver.common.action_chains import ActionChains

import time
import json
import requests
#等待第一个
#显示等待
from selenium.webdriver.support.ui import WebdriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expected_conditions


from lxml import etree
web = Firefox()

def get_page_src(url):
    web.get(url)

    el = WebdriverWait(web,10,0.5).until(#until发现唤醒--结束等待的条件
        EC.presence_of_element_located((By.XPATH," "))#第一个的xpath
    )

    page_source = web.page_source
    web.quit()      #quit
    return page_source 
def get_job_name(page_source):
    tree = etree.HTML(page_source)
    job_names = tree.xpath(" .../text()")
    print(job_names)

if __name__ == '__main__':
    source = get_page_src(" ")
    get_job_name(source)
