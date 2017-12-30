__author__ = "JJ.sven"

import multiprocessing
from  multiprocessing import Queue, Process, Pipe, Manager
import os

'''进程间通讯
不同进程间内存是不共享的，要想实现两个进程间的数据交换，可以用以下方法
1. Queue

进程间通过传递Queue，共享数据
实际上是传递过程中，Queue克隆了一份，它们的数据实际是序列化后共享的，取的时候再反序列化，
也就是Queue 和 它 克隆的Queue，共享同一份序列化的数据

2. pipe 管道，类似socket，一发一收

3. Manager
A manager returned by Manager() will support types 
=> list, dict, Namespace, Lock, RLock, Semaphore, BoundedSemaphore, 
Condition, Event, Barrier, Queue, Value and Array. For example,

内部又互斥锁功能，所以不需要加锁
'''

def f(n, q):
    q.put(['jj', 2, 'xx'])
    print( n, 'processing edit q --')

def f_pipe(n, conn):
    conn.send('data from sub process')
    print(conn.recv())
    conn.close()

def f_manager(d, l):

    d[os.getpid()] = 'pid'
    l.append(1)
    print(l)


if __name__ == '__main__':
    print('''queue
    ''')
    q = Queue()
    p = Process(target=f, args=('子进程', q))
    p.start()
    print('父进程 get q', q.get())

    print('''pipe
    ''')
    cur_conn, sub_conn = Pipe()
    p2 = Process(target=f_pipe, args=('子进程', sub_conn))
    p2.start()
    print(cur_conn.recv())
    cur_conn.send('data from sup')
    cur_conn.close()

    print('''manager
    ''')
    with Manager() as manager:
        d = manager.dict() #共享的

        l = manager.list(range(5))
        p_list = []
        for i in range(10):
            p = Process(target=f_manager, args=(d, l))
            p.start()
            p_list.append(p)
        for res in p_list:
            res.join()

        print(d)
        print(l)