import asyncio

async def func1():
    print("func1")  
    await asyncio.sleep(1)
    print("func1 over")
    return "func1 返回值"

async def func2():#协程  生成器
    print("func2") 
    await asyncio.sleep(2)
    print("func2 over")
    return "func2 返回值"

async def func3():#协程  生成器
    print("func3") 
    await asyncio.sleep(3)
    print("func3 over")
    return "func2 返回值"

async def main():
    f1 = func1()
    f2 = func2()
    f3 = func3()

    tasks = [
        asyncio.create_task(f1),
        asyncio.create_task(f2),
        asyncio.create_task(f3),
        ]
    result =  asyncio.gather(*tasks) #(*tasks,return_exceptions =Flase) 
    #return_exceptions= True，如果有错误信息。返回错误信息，其他任务正常执行.
    #return_exceptions= False，如果有错误信息，所有任务直接停止


    #位置参数   有顺序   
    #结束,运行

    #done,pending = await asyncio.wait(tasks)#第二
    
    #print(done)
    #print(pending) 空
    """
    for t in done:
        print(t.done())#done set集合 无序 返回结果没有顺序
    """
   

if __name__ == "__main__":
    asyncio.run(main())
