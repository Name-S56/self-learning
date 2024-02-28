from selenium.webdriver import Firefox
web=Firefox  ()
web.get("wbdy.tv")

#切换道iframe (框架子页面)_
iframe =  web.find_element_by_xpath('xx')
web.switch_to.frame(iframe)

input = web.find_element_by_xpath('xxx')
placeholder = input.get_property('placeholder')
print(placeholder)

#跳出iframe 
web.switch_to.parent_frame()#dad
content = web.find_element_by_xpath('xx').text

#还能下拉列表selenium