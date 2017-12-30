__author__ = "JJ.sven"

import threading
import queue
import time

count = 0

def producer():
    global count
    for i in range(10):
        count += 1
        q.put("骨头 %s" % i)

    print("开始等待所有的骨头被取走...")
    q.join()
    print("所有的骨头被取完了...")
    if count < 20:
        time.sleep(2)
        print('继续生产')
        producer()

def consumer(n):
    while True:
        print("%s 取到" % n, q.get())
        time.sleep(1.0)
        q.task_done()  # 告知这个任务执行完了


q = queue.Queue()

p = threading.Thread(target=producer)
p.start()

c1 = threading.Thread(target=consumer, args=("李闯",))
c1.setDaemon(True)
c2 = threading.Thread(target=consumer, args=("韩斌",))
c2.setDaemon(True)
c1.start()
c2.start()
