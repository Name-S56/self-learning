import requests
#提取IP
def get_ip():   #有待完善,IP拿完了怎么办
    url ="API链接"
    resp = requests.get(url)
    ips = print(resp.json())
    for ip in ips['data']['proxy_list']:
        yield ip #一个一个返回代理IP    生成器


def spider(url):
    url=""
    while 1:
        try:
            proxy_ip = next(gen)
            proxy={
                "http":"http://"+ proxy_ip,
                "https":"https://"+ proxy_ip,
            }
            resp = requests.get(url)
            resp.encoding="utf-8"
            return resp.text
        except:
            print("error")
            
if __name__ == '__main__':
    gen = get_ip()  #gen就是IP的生成器
    for i in range(10):
    spider()