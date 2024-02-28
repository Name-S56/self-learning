from selenium.webdriver import Firefox
driver = Firefox() 
driver.get('https://www.baidu.com')

print(driver.title) #固定获取title