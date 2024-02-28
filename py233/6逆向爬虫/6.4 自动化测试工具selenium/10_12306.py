from selenium.webdriver import Firefox
import json
import request

from selenium.webdriver.common.action_chains import ActionChains

def base64_api(img,typeid=27,uname="qwewew",pwd="qwqwqw"):

    data = {"username": uname, "password":pwd, "typeid":typeid, "image":img}
    result = json.loads(
        requests.post("http://api.ttshitu.com/predict",json = data).text
    )
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]
    
web = Firefox()
web.get(" ")

web.implicitly_wait(10)

web.find_element_by_xpath(' ').click()
web.find_element_by_xpath('').send_keys("123456")
web.find_element_by_xpath('').send_keys("pwd")

#验证码
img = web.find_element_by_xpath(' ')
b64_verify_img = img.screenshot_as_base64

result = base64_api(b64_verify_img)

for p in result.split("|"):
    x = p.split(",")[0]
    y = p.split(",")[1]
    ActionChains(web).move_to_element_with_offset(img,x,y).click().perform()
    time.sleep(1)

web.find_element_by_xpath(' ').click()

'''以下为12306 特有 滑块验证'''

btn = web.find_element_by_xpath(' ') #找按钮
ActionChains(web).drag_and_drop_by_offset(btn,xoffset=300,yoffset=0).perform() #抓着移动
# ActionChains(web).click_and_hold(btn).move_by_offset()  #2种方法

'''why error?'''
 #selenium 被检测了
#selenium 特征  window.navigator.webdriver = true 
#according to your browser
