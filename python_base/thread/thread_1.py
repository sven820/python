__author__ = "JJ.sven"

import time
import threading

'''
* 两种线程开启方式，1 threading.Thread（）2 继承threading.Thread，重写run方法
* join的使用  
* 守护线程和非守护线程 setDaemon
'''

def task(t):
    print(t)
    time.sleep(2.0)

t1 = threading.Thread(target=task, args=('t1',))
t2 = threading.Thread(target=task, args=('t2',))

# t1.start()
# t1.join() #等待线程执行完毕，加了这个，就得t1执行完毕在执行t2
# t2.start()

class MyThread(threading.Thread):

    def __init__(self, task):
        super(MyThread, self).__init__()
        self.task = task

    def run(self):
        print(self.task +' running task')
        time.sleep(2)

t3 = MyThread('task3')
t4 = MyThread('task4')
# t3.start()
# t4.start()

start = time.time()
tasks = []
for i in range(50):
    t = threading.Thread(target=task, args=('task_' + str(i),))
    ''' # 把当前线程设置为守护线程，需在start之前设置
        这里主程序的结束需要等子线程都结束了才会结束程序
        
        如果把当前子线程设置为守护线程，则主程序的退出不依赖守护线程是否结束，
        主程序结束了，守护线程就结束了
        
        例如socketserver，每个conn都是守护线程，主线程不依赖子线程是否还在执行，可直接退出结束程序
    '''
    # t.setDaemon(True)
    t.start()
    tasks.append(t)
for t in tasks:
    t.join()
end = time.time()
print(threading.active_count())
print(threading.current_thread())
print('time: ', end - start)

