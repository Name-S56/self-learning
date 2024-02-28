import asyncio


async def download(url,t):
    print("start")
    await asyncio.sleep(t)
    print("over")

async def main():
    urls=[
        "http://",
        "http://",
        ]
    tasks = []
    for url in urls:
        task = asyncio.create_task(download(url,3)) #除警告
        tasks.append(task)
    #统一等到协程任务1完毕
    await asyncio.wait(tasks)   #warning

if __name__ == "__main__":
    asyncio.run(main())


#扫url
#循环url,创建任务
#统一await