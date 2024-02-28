import re
import requests
from datetime import datetime

domain = "https://api.zhihu.com/articles/"
url = "https://www.zhihu.com/api/v4/search_v3?gk_version=gz-gaokao&t=general&q=web3.0&correction=1&offset=0&limit=20&filter_fields=&lc_idx=0&show_all_topics=0&search_source=Normal"
headers ={
    "Accept":"*/*",
    #"Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cookie":"_zap=bdad7352-539a-4580-93d4-35f93e4f80bd; d_c0=ACDXYu830haPTtVWbA9vlzOIUrX3_-f2OBQ=|1684844646; __snaker__id=OWXUiO4GGKSsmQT1; YD00517437729195%3AWM_NI=1zAD65b44VtLAPPLiHp8YnhdEIM4x6DOufkIux%2Bv9E50aY3mXCB6pRrMxUqbd0jXz48sOefAZTL3wNkK%2FWHX2CQMO35vOb%2FBvt8d32aPVC1kl32EHhHXOdjvLEbFvD9rdmo%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6ee99f768aa9900d0e87b87968fb7c54b968a8b83d174818da5afe869acb898b0d22af0fea7c3b92af3a68fa5b53fa2ecfcb7f7488390a0adec44b4e8978feb70879783d5fb3e8891bb87ea43b7a8e597bc4ff7f0afbab2679c9d8ed7f35ab293b8b6f46aa8f0a6b9f940fcad8186e54b9a8c84d4f646a995e1b8cb54f29d9faece39f7aa8183ae4ab6acf885b23aa3909aa4b461b0edfea6cb648c888185e97e909baea7f550fbaeac8eee37e2a3; YD00517437729195%3AWM_TID=sMx1eLgCYXRAQQEUQBOQ0GXlYfdxwTaG; q_c1=c5ef29343c9a43d6ad8952f512f5be26|1684907318000|1684907318000; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1689757105,1689757817; _xsrf=q4uSnHe8HomWNFJkGUvK5VfF3DntbhOK; z_c0=2|1:0|10:1699864720|4:z_c0|80:MS4xTThSd1BnQUFBQUFtQUFBQVlBSlZUWkF1UDJiUExhaGZfeDBuR2pPMUY3ekVZYXp2MjUzelJBPT0=|9da7a67308e6501aa02db22953dae6f6ce263d4f0b02b7b0b9d88a2661cae2ae; SESSIONID=P2lipnKR5A1mL3ufn2am3rpHADrTqCqlxc1zz6YWPj9; unlock_ticket=ANCXx5vdnxUmAAAAYAJVTR7rUWUpuut-Umc2vE6VKFdX1RRCc65XgA==; KLBRSID=fe78dd346df712f9c4f126150949b853|1699865622|1699862151",
    "Dnt":"1",
    "Referer":"https://www.zhihu.com/search?type=content&q=web3.0",
    "Sec-Ch-Ua":'"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    "Sec-Ch-Ua-Mobile":"?0",
    "Sec-Ch-Ua-Platform":"Windows",
    "Sec-Fetch-Dest":"empty",
    "Sec-Fetch-Mode":"cors",
    "Sec-Fetch-Site":"same-origin",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "X-Api-Version":"3.0.91",
    "X-App-Za":"OS=Web",
    "X-Requested-With":"fetch",
    "X-Zse-93":"101_3_3.0",
    "X-Zse-96":"2.0_AXd5sA8=otL/UkRtni8I6J6b2F=lAo48h3+3rP6jyU6KA5woxAmDH=LOtLqFQ78e",
    "X-Zst-81":"3_2.0VhnTj77m-qofgh3TxTnq2_Qq2LYuDhV80wSL7iUZQ6nxEHY0m4fBJCHMiqHPD4S1hCS974e1DrNPAQLYlUefii7q26fp2L2ZKgSfnveCgrNOQwXTt_Fq6DQye8t9DGwT9RFZQAuTLbHP2GomybO1VhRTQ6kp-XxmxgNK-GNTjTkxkhkKh0PhHix_F0PVaCL0MXoGPhLL2wCBz9tmm9X1bwOGk8eM1vxOHUC1IUS0ZJO8NGCLuUL0FH_z-wgMJHtmRJHKoirCUG3Ky9HBpB2YbHSYjgSXeUxM4wOyWvVqEuFsoLpOyrXygrOOyCeVS8wOiDN8fc30HJSMEwSYvrL820VCVwYskceMghFfQ7SLurxs",
    }
resp = requests.get(url,headers=headers)
resp.encoding=resp.apparent_encoding
pageSource = resp.text
obj = re.compile(r'"type":"search_result".*?"title":"(?P<title>.*?)"}.*?https://api.zhihu.com/articles/(?P<id>.*?)"'
                 r'.*?"content":".*?u003e(?P<content>.*?)",',re.S)
result = obj.finditer(pageSource)
name = datetime.now().strftime("%m月_%d日")
with open(f"{name}.md",mode="w",encoding='utf-8')as f:
    for item in result:
        child_url = domain +item.group("id");
        child_resp = requests.get(child_url)
        child_resp.encoding="utf-8"
        content = re.compile(r'"content":"(?P<content>.*?")',re.S)
        title = item.group("title")
        new_title = re.sub(r"\\u003c.*?\\u003e", " ", title)
        content = item.group("content")
        new_content = content.replace("\\u003cbr/\\u003e","\n")
        new_content = re.sub(r"\\u003c.*?\\u003e", "   ", new_content)
        f.write("### "+new_title+'\n'+\
            "**url: **"+domain+item.group("id")+'\n'+ 
            "**content: **\n"+new_content+'\n\n')
    f.close()