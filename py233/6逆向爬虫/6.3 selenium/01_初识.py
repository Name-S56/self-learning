#selenium 自动化测试
#自动打开浏览器
#输入网址
#能从页面提取东西
#先确定 chrome

#杂牌浏览器 没有:)
        #from selenium import webdriver
#浏览器需要 驱动程序
from selenium.webdriver import Chrome
#创建浏览器对象

web = Chrome()  #不用加executable_path 不加参数自动查找浏览器驱动
#打开网址
url = "https://www.baidu.com/"
web.get(url)



print(web.title) #固定获取title