#BOSS直聘 防爬虫  返回状态码  302重定向
#request 噩梦


#1可以选择先登录．登录后.放慢抓取速度  (谨慎封号,不登陆速度慢)  详细看md
from selenium.webdriver import Firefox
#事件链
from selenium.webdriver.common.action_chains import ActionChains
web = Firefox()
web.get("http://login.zhipin.com/?ka=header-login")

web.implicitly_wait(10)

web.find_element_by_xpath('//*[@id="wrap"]/div/div[2]/div/div[2]/div[1]/div[1]/div/span[2]/input').send_keys('186xxxx')#用户名
web.find_element_by_xpath('//*[@id="wrap"]/div/div[2]/div/div[2]/div[1]/div[2]/div/span/input').send_keys('xxxx')#密码
web.find_element_by_xpath('').click()

#获取到验证码图片的div
verify_div = web.find_element_by_xpath('')
verify_div.screenshot("tu.png")
tu = verify_div.screenshot_as_base64 #截图screenshot

verify_code = base64_api(tu)    #图鉴   开始识别
print(verify_code)

for p in verify_code.split("|"):
    x = int( p.split(",")[0])
    y = int( p.split(",")[1])

    ActionChains(web).move_to_element_with_offset(verify_div, xoffset=x,yoffset=y).click().perform() #perform提交事件
    time.sleep(1)

web.find_element_by_xpath('').click() #点击确认



