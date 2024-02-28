from threading import Thread


#创建任务
def func(name):
    for i in range(10):
        print(name,i)


if __name__ == '__main__':
    #创建线程
    t1 = Thread(target = func,args=("一一一",)) 
        #Thread类的构造函数             args 必须要求元组--字符串
        #                         甚至可以args=(arg1,arg2)
    t2 = Thread(target = func,args=("二二二",))
    t1.start()
    t2.start()
    print("我是主线程")
    #1个主线程  2个副线程