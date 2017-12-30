__author__ = "JJ.sven"

import threading
import time
import random

'''互斥锁 mutex
   3.0应该是做了优化（估计只是简单计算不会出问题，复杂task多线程间应该也会出现数据线程不安全）
   所以问了保证数据在多线程间的安全问题，有时候要给修改数据的步骤加同步锁，并且步骤不能太耗时
'''
def run(n):
    lock.acquire()
    global  num
    num +=1
    # 加了锁就等于之间的操作是串行的，如果有耗时操作，等于累加这些耗时，多线程时就会出现等待
    # time.sleep(1)
    lock.release()


lock = threading.Lock()
num = 0
t_objs = [] #存线程实例
for i in range(50):
    t = threading.Thread(target=run,args=("t-%s" %i ,))
    t.start()
    t_objs.append(t) #为了不阻塞后面线程的启动，不在这里join，先放到一个列表里

for t in t_objs: #循环线程实例列表，等待所有线程执行完毕
    t.join()

print("----------all threads has finished...",threading.current_thread(),threading.active_count())

print("num:",num)