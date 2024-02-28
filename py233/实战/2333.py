import requests

url = "https://www.zhihu.com/api/v4/search_v3?gk_version=gz-gaokao&t=general&q=%E7%A7%81%E5%9F%9F&correction=1&offset=0&limit=20&filter_fields=&lc_idx=0&show_all_topics=0&search_source=Normal"
headers = {
    "authority": "www.zhihu.com",
    "method": "GET",
    "path": "/api/v4/search_v3?gk_version=gz-gaokao&t=general&q=%E7%A7%81%E5%9F%9F&correction=1&offset=20&limit=20&filter_fields=&lc_idx=20&show_all_topics=0&search_hash_id=e6f802480fe4f69ff01925ed95e675ef&search_source=Normal&vertical_info=0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C4",
    "scheme": "https",
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cookie": "_zap=3132cbe6-815f-4dcb-aea1-ac8e18ea5e9d; d_c0=ABARm0yVXhePTlFub5oJ8GMcbeskOWXMbRU=|1694264362; __snaker__id=8Edf9tM34jTeR34V; YD00517437729195%3AWM_TID=Fvg7HFXasoNEFRQARFfViGq03m%2B8%2FIaY; YD00517437729195%3AWM_NI=%2BEdswGyvw8ED5%2FNFMrnPQT18JfFzXDf%2BTBroFPSa4eq5u7xIsq2FvcFuAcbRrNZUqVaQsGftyJlpJH4BEEGrEvC%2FDVzDGtQFZyjs9%2FPpRd2EF6UE3yfDn27M4ixfbgjfNk4%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eeadb561fc8c8ed1e868b78a8eb3c14b878a8f82c4398bbca0d4eb3ff8ecac88f62af0fea7c3b92ae99bac94f64dbbaab9d9c850f7f182a7d07aae909fb5b4348aba8a9bdb50a6f59ca3f16586909d82b76fb3ebbbd8fb43b1affea7f56986ab8f84e15ab29296b6f45ea38fbda8e580bb96a491c944f89e8ba6c67a87aa8dd0c75eba9c8995d44e9aa7a694bc2594b09e85b14f86ea9ba6b273a69ca2d3b647f8b7b887e16daaba828cb737e2a3; q_c1=4c8938f241114a67a77d3afb92ffcad3|1694748282000|1694748282000; _xsrf=t7z0OOoGnlGYmWYG7u7qyHZJR5fuW1CM; z_c0=2|1:0|10:1699443561|4:z_c0|80:MS4xMjhReENBQUFBQUFtQUFBQVlBSlZUV25CT0daOE5PamtKR3p1alJxY0pBMFEycEJoVFNlTWNBPT0=|b72913cbe91a1cdb61180a63368425327d4d00fc11ee5910153d3c36c29e104c; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1699443562,1699781953,1699880779,1700119417; tst=r; SESSIONID=enAuyzRFkOxl3L9xxk6idzNB2Oj9PDPg4bLdWufKwOO; JOID=UlEVAUqV5mIWcci9bpf-88M-X-t5-YEhYAm75ir_oBN4QYWNH-4uNnF5yLZvR9Ft5fp06GdKfQiQQ6Af7LG-5hg=; osd=UlEVAkyV5mIVd8i9bpT488M-XO15-YEiZgm75in5oBN4QoONH-4tMHF5yLVpR9Ft5vx06GdJewiQQ6MZ7LG-5R4=; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1700119467; KLBRSID=d017ffedd50a8c265f0e648afe355952|1700119467|1700119396",
    "Referer": "https://www.zhihu.com/search?type=content&q=%E7%A7%81%E5%9F%9F",
    "Sec-Ch-Ua": "\"Microsoft Edge\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
    "Sec-Ch-Ua-Mobile": "?1",
    "Sec-Ch-Ua-Platform": "\"Android\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "X-Api-Version": "3.0.91",
    "X-App-Za": "OS=Web",
    "X-Requested-With": "fetch",
    "X-Zse-93": "101_3_3.0",
    "X-Zse-96": "2.0_F4xUBPG3VPhZt6FWHWp2OF7fgmgBg0FcHWa4uy8wrIV1mXFGgzy6QiG=P0pArI6r",
    "X-Zst-81": "3_2.0aR_sn77yn6O92wOB8hPZnQr0EMYxc4f18wNBUgpTQ6nxERFZYXY0-4Lm-h3_tufIwJS8gcxTgJS_AuPZNcXCTwxI78YxEM20s4PGDwN8gGcYAupMWufIeQuK7AFpS6O1vukyQ_R0rRnsyukMGvxBEqeCiRnxEL2ZZrxmDucmqhPXnXFMTAoTF6RhRuLPFXO9dhgYkUgqXqNVWC2mjGwO6Q99XUtxWgLOgDO8rDwq8GC8rqxC4wS9NcSTv_tKcek9NGFOqr9L9gOVgDXBJBt06rCqeBeXfu3CNgVqxhOYe92uTbeYwwwqyUSmc6S_cMYmqDC1wqVZcXYB8cfYf7tqLDg8bHNXHBCfpCFCbwL_OCH9CqfzK7xqoMH8oicKrhCOpGVBzuS9eXFLN92mx93LQuN8jUp1TcLMBcn9qCOOfgFVfvOqGHpqjqeB1rSKBUtqmekCoHcM6_FKcXO0pUtBYgLmoLcLChLLuwYC"
}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    data = response.json()
# # 解析json数据并提取所需的标题、内容和文章详细url
    for item in data["data"]:
            title = item["object"]["title"]
            content = item["object"]["content"]
            url = item["object"]["url"]
            print(title,content,url)
            with open("data.md", "a", encoding="utf-8") as file:
                file.write(f"## {title}\n")
                file.write("### 内容\n")
                file.write(content+"\n")
                file.write(f"##$ 文章详细url:{url}")
# # 将提取到的数据保存到md文件中
else:
    print("请求失败:", response.status_code)
