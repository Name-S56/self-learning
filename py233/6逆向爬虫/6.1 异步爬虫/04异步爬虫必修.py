import asyncio
import aiohttp
import aiofiles
# aiohttp , aiofiles文件读写

async def download(url):
    file_name = url.split("/")[-1]
    async with aiohttp.ClientSession() as session:#相当于requests  with自动关闭
        #发送网络请求
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        }
        async with session.get(url,headers)as resp:#headers
            # await resp.text()
            content = await resp.content.read()
            #await resp.json()

            #写入文件
            async with aiofiles.open(file_name,"wb") as f:
                await f.write(content) 

async def main():
    url_list=[
        "",
        "",
        ]
    tasks=[]
    for url in url_list:
        t = asyncio.create_task(download(url))
        tasks.append(t)


if __name__ == "__main__":
    asyncio.run(main())