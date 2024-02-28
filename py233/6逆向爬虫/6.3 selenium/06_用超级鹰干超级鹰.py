from selenium.webdriver import Firefox
from chaojiying import Chaojiying_Client

web = Firefox()
#拿验证码图
web.get("  ")


png = web.find_element_by_xpath(' ').screenshot_as_png