__author__ = "JJ.sven"

'''进程锁 （进程同步）
 
 防止进程间抢输出资源  ==》 屏幕打印乱序
'''

from multiprocessing import Process, Lock


def f(l, i):
    l.acquire()
    try:
        print('hello world', i)
    finally:
        l.release()


if __name__ == '__main__':
    lock = Lock()

    for num in range(10):
        Process(target=f, args=(lock, num)).start()