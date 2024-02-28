import asyncio

async def func2():
    print("func2 ")
    await asyncio.sleep(2)
    print("func2 over")

async def func1():
    print("func1 ")
    await asyncio.sleep(1)
    print("func1 over")

async def func3():
    print("func3") 
    await asyncio.sleep(3)
    print("func3 over")

if __name__ == "__main__":
    loop = asyncio.get_event_loop() #asyncio.get_event_loop()

    task1 = loop.create_task(func1()) # 创建任务
    task2 = loop.create_task(func2())
    task3 = loop.create_task(func3())

    tasks = [
        task1, 
        task2, 
        task3
        ]

    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    