import requests

content = input ('请输入你要检索的内容')
url = f"https://www.sogou.com/web?query={content}"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76"
}
resp = requests.get(url)
print(resp.text)
print(resp.request. headers)#查看请求头信息
