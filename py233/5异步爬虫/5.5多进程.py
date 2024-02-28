from multiprocessing import Process

def func (name):
    for i in range(100):
        print(name,i)

if __name__ == '__main__':
    p2 = Process(target=func,args=("222"))
    p1 = Process(target=func,args=("111"))
    p1.start()
    p2.start()

#多线程 多进程?
#多进程不常用

#1.多线程:  任务统一.
#2 多进程:  多任务相对独立,很少有交集.