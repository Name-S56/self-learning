from selenium.webdriver import Edge
import time 
from selenium.webdriver.common.keys import Keys
web=Edge()
web.get("http://www.lagou.com")


# 找X 关闭
x_btn= web.find_element_by_xpath('//*[@id="cboxClose"]')   #复制XPATH 
x_btn.click()
#需要休息
time.sleep(1)#低级low 方法 暂时使用
#如正常人  找输入框   输入    点击搜索
web.find_element_by_xpath('//*[@id="search_input"]').send_keys("python",Keys.ENTER) #输入框 python java

time.sleep(2)

    #selenium可以动态执行js
web.execute_script("""
        var a = document.getElementsByClassName("un-login-banner")[0];   
        a.parentNode.removeChild(a); 
    """)
li_list  = web.find_elements_by_xpath('//*[@id="s_position_list"]/ul/li') #elements多个值

for li in li_list:
    h3 = li.find_element_by_xpath("./div[1]/div[1]/div[1]/a/h3")
    #print(h3.text)
    h3.click()
    #已经看到详情页,但是selenium需要调整视角  ,切换窗口
    web.switch_to.window(web.window_handles[-1])  #window frame parent_frame
                        #整页面最后一个(最新的一个)
    job_detail = web.find_elements_by_xpath('//*[@id=""]')
    txt = job_detail.text #文本
    print(txt)
    time.sleep(1)
    #关闭该窗口
    web.close()
    #调整selenium视角
    web.switch_to.window(web.window_handles[0])
    break
web.quit()
        #consloe 里写js  
"""
    var a = document.getElementsByClassName("un-login-banner")[0];   整页面查询 通过by   Class
    a.parentNode.removeChild(a); 
    """

