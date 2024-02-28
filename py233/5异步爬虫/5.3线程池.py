from concurrent.futures import ThreadPoolExecutor

def func(name):
    for i in range(10):
        print(name,i)
        return name
    
def fn(res):
    print(res.result())

if __name__ == '__main__':
    with ThreadPoolExecutor(10) as t:
        '''
        for i in range(100):
            t.submit (func, f"num{i}").add_done_callback(fn)   #返回   即执行 callback函数   顺序不确定
            #绑定fn函数   fn 返回值-result()?   返回值顺序不确定
    '''
        result = t.map(func,["111","222","333"])
        for r in result:
            print(r)
            # map 返回值为生成器,返回顺序一致