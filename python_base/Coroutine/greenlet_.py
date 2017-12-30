__author__ = "JJ.sven"

from greenlet import greenlet
import gevent

print('''greenlet 手动切换 \n''')

def fun1():
    print('do fun1 before')
    gr2.switch()
    print('do fun1 after')
    gr2.switch()

def fun2():
    print('do fun2 before')
    gr1.switch()
    print('do fun2 after')
    gr1.switch()

gr1 = greenlet(fun1)
gr2 = greenlet(fun2)
gr1.switch()

print('''\n gevent 自动切换 \n''')

def fun1_auto():
    print('do fun1 before')
    gevent.sleep(2.0)  # 模仿IO操作
    print('do fun1 after')

def fun2_auto():
    print('do fun2 before')
    gevent.sleep(1.0)
    print('do fun2 after')

gevent.joinall(
    [
        gevent.spawn(fun1_auto),
        gevent.spawn(fun2_auto)
    ]
)