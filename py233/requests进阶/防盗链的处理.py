import requests
#1。拿到contId
#2。拿到videoStatus返回的json.  ->  srcURL
#3. srcURL里面的内容进行修整
#4，下载视频

url = "https://www.pearvideo.com/video_1787592"
contId = url.split("_")[1]#切割上面的url 拿到1787592
 
videoStatus = f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.17068459506292188"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0",
    #防盗链:溯源请求的上一级
    "Referer" : url
    }
resp = requests.get(videoStatus,headers=headers)
dic=resp.json()

srcUrl = dic['videoInfo']['videos']['srcUrl']   #Preview
systemTime = dic['systemTime']

srcUrl = srcUrl.replace(systemTime,f"cont-{contId}")#f{}
print(srcUrl)
#下载视频
'''
with open ("1.mp4",mode="wb")as f:
    f.write(requests.get(srcUrl).content)
    '''

