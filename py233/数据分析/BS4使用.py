from bs4 import BeautifulSoup

html="""
<ul>
</ul>
"""

#初始化beautifulSoup对象
page = BeautifulSoup(html,"html.parser")    #上面的html变量,html.parser解析器 
#page.find("标签名",attrs={"属性":"值"})
page.find("li",attrs={"id":"abc"}) #只找到一个
#page.find_all("标签名",attrs={"属性":"值"}) 找到一堆结果
li.find("a")   #查找后,可再次查找

print(a.text)
print(a.get("href"))
