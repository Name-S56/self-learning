import requests

url = "https://fanyi.baidu.com/sug"

data_name = {   #可改名
    "kw":input('输入一个单词')
}

resp = requests.post(url,data=data_name)#赋值

#print(resp.text)
print(resp.json())  #json数据