__author__ = "JJ.sven"

import multiprocessing
import threading
import time
import os

'''进程 多进程解决python实际在操作系统上实际为单线程处理任务，资源利用率低的问题
1. 至少包含一个线程
2. 每个子进程都由父进程启动
'''

def thread_run():
    print('thread_run: ', threading.get_ident())

def run(n):
    print(n, '--run---进程ID：%s--父进程ID：%s️' % (os.getpid(), os.getppid()))
    t = threading.Thread(target=thread_run)
    t.start()
    time.sleep(2)

processes = []
for i in range(10):
    p = multiprocessing.Process(target=run, args=(str(i),))
    p.start()
    processes.append(p)

for p in processes:
    p.join()

run('current')
