import requests
from bs4 import BeautifulSoup
from datetime import datetime

url="https://e-hentai.org/news.php"
resp = requests.get(url)
resp.encoding="utf-8"
print(resp.text)