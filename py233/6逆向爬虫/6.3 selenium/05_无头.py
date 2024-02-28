from selenium.webdriver import Firefox
import time 
from selenium.webdriver.support.select import Select # 下拉列表 <select>


web=Firefox  ()
web.get("")


sel = web.find_element_by_xpath('')
sel_new = Select(sel)

sel_new.select_by_index()  #位置
# sel_new.select_by_value()  #value值
# sel_new.select_by_visible_text()  #展示文字

print(sel_new.options) #options  sssss复数
"""
<select>
    <option value='2021'>2021年</option>  --给用户展示2021年  selenium选择2021
    <option value='2020'>2021年</option>
</select>
"""
for i in range(len(sel_new.options)):
    sel_new.select_by_index(i)
    time.sleep(3) #太快拿不到  笨方法 
    #切换完
    trs = web.find_element_by_xpath('//*[@id="TableList"]/table/tbody/tr')
    for tr in trs:
        print(tr.text)


#获取页面代码   (不是页面源代码  F12内元素代码)
page_src = web.page_source
print(page_src)
#selenium 缺点就是慢