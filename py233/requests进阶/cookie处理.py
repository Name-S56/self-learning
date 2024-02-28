# 登陆 ->cookie
#cookie 去请求url -> 内容

#使用session 进行请求 -> 一连串的请求
#session 会话
import requests
session = requests.session()
data ={
    "loginname":"",
    "password":""
}

#login
url= ""
resp = session.post(url,data=data)

#print(resp.cookies) 看cookie
#书架数据 url
session.get('')#放url
#print(resp.json())

''''
resp =erquests.get("",headers={
    "cookie":""
})
'''