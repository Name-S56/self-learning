import requests
url=""
proxy={
	"http": "http://xx.xx.xx.xx:xx",
	"https": "https://xx.xx.xx.xx:xx",
}

resp = requests.get(url,proxies = proxy)
resp.encoding='utf-8'
print(resp.text)
