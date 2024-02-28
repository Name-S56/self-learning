from threading import Thread

class MyThread(Thread):
    def __init__ (self,name):#init 传参
        super(MyThread,self).__init__()#初始化
        self.name = name

    def run(self): #run方法 -->返回值可不写
        for i in range(10):
            print(self.name,i)

if __name__ == '__main__':
    t1 = MyThread("一一一")
    t2 = MyThread("二二二")
    t1.start()
    t2.start()

