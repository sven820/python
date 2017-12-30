__author__ = "JJ.sven"

''' event

- set()设置信号
使用Event的set()方法可以设置Event对象内部的信号标志为真。
Event对象提供了is_set()方法来判断其内部信号标志的状态，
当使用event对象的set()方法后，is_set()方法返回真.

- clear() 清除信号
使用Event对象的clear()方法可以清除Event对象内部的信号标志，即将其设为假，
当使用Event的clear方法后，is_set()方法返回假

- wait（）等待
Event对象wait的方法只有在内部信号为真的时候才会很快的执行并完成返回。
当Event对象的内部信号标志位假时，则wait方法一直等待到其为真时才返回。
'''

import threading,time
import random


def light():
    count = 0
    event.set() # 绿灯开
    print('绿灯开， 红灯关')

    while True:
        if count > 10:
            count = 0
            event.set()  # 绿灯开
            print('绿灯开， 红灯关')
        elif count > 5:
            if event.is_set():
                event.clear()  # 绿灯关
                print('绿灯关， 红灯开')



        time.sleep(1)
        count += 1

def car():

    while True:
        # if event.is_set():
        #     print('car run')
        # else:
        #     print('car stop')
        # time.sleep(1)

        if event.is_set():
            print('car run')
            time.sleep(1)
        else:
            print('car stop')
            event.wait() # 后面不会执行了，会卡在这



if __name__ == '__main__':
    event = threading.Event()
    light_t = threading.Thread(target=light)
    light_t.start()

    for i in range(3):
        t = threading.Thread(target=car)
        t.start()