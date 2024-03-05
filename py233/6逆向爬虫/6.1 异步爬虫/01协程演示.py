import asyncio  #借助event_loop

async def func():#协程  生成器
    print("233") 

 
if __name__ == "__main__":
    result = func()
    #print(result)
    
    asyncio.run(result)#loop.close()可能报错
    #同下
"""   
    event_loop = asyncio.get_event_loop()
        #event_loop执行协程对象,直到该对象内容执行完毕
    event_loop.run_until_complete(result)
"""
