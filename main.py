import requests
 
def check_proxy(proxy):
    try:
        res = requests.get('https://zlibrary-asia.se/', proxies=proxy, timeout=5)
        if res.status_code == 200:
            return True
        else:
            return False
    except:
        return False