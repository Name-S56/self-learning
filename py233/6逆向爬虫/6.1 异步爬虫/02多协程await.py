import asyncio  #借助event_loop
import time

async def func1():
    print("func1")  
    await asyncio.sleep(1)
    print("func1 over")

async def func2():#协程  生成器
    print("func2") 
    await asyncio.sleep(2)
    print("func2 over")


async def func3():#协程  生成器
    print("func3") 
    await asyncio.sleep(3)
    print("func3 over")

#多函数任务
 
if __name__ == '__main__':
    start = time.time()
    task1 = func1()
    task2 = func2()
    task3 = func3()
    #三个任务放一起
    tasks = [
        task1,
        task2,
        task3,
        ]
    asyncio.run(asyncio.wait(tasks)) #无阻塞
    """print(time.time() - start())"""
    #await 挂起