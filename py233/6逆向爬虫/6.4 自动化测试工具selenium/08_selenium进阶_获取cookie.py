from selenium.webdriver import Firefox

web = Firefox()
web.get("http://www.baidu.com")

cookies  = web.get_cookies()
print(cookies)
#a = sdadasdas;b =asdasdasd
#cookies 键值对
#{'name': 'DAIDUID_BFESS', 'value': '54C5.....:FG=1'}

#转成python的字典
'''{
    'DAIDUID_BFESS' :'54C5.....:FG=1'
}'''
cookie_dic ={}
for dic in cookies:
   key = dic['name']
   value = dic['value']
   cookie_dic[key] = value

cookie_dic = {
   dic[' name']: dic['value'] for dic in cookies
             }#字典生成式->列表生成式

#当你已经有了一个字典形式的cookie，可以直接把这个字典作为参数传递给requests
import requests
headers = {}        #直接把cookies当成参数传递即可(必须是字典)
requests.get("xxxx",headers=headers,cookies=cookie_dic)

# 增量式爬虫++
"""## 关于等待

1. **`time.sleep()`** 

   干等

2. **`web.implicitly_wait()`**

   元素加载**出来**后继续<!--不能选中不算--> ; 未加载则等待一段时间。全局设置

   `web.implicitly_wait(10)`    最多等10s	<!--隐士等待-->

3. **WebDriverWait**
   单独等一个元素, 出现,pass; 超时,error		<!--显示等待,(等待对象,10s最大,0.5间隔)-->
   ele= WebDriverWait(web,10,0.5).until(	
    #EC.presence_of_element_located((By.XPATH,"/html/body/div[5]/div[2]/div[1]/div/div"))`
    ) 
"""
