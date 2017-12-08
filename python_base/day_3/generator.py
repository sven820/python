__author__ = "JJ.sven"

import time

#列表生成
list = [i * 2 for i in range(10)]
print(list)

#生成器，一边循环一边计算的机制，只有在调用的时候才能获得到具体的值

ger = (i * 2 for i in range(1000))
print(ger)
print(next(ger))

for i in ger:
    pass
    # print(i)



def fib(n):
    index, a, b = 0, 0, 1
    while index < n:
        # print(b)
        yield b
        a, b = b, a + b
        index += 1

for i in fib(10):
    print(i)

# yield 返回后，下次从上次结束地方开始
'''
def yield_test():
    yield 1
    yield 2
    yield 3
t = yield_test()
print(next(t))
print(next(t))
print(next(t))

'''

# yield 应用，单线程下并发处理（协程）
print('协程demo'.center(50, '-'))

def consumer(name):
    print('准备吃包子')
    while True:
        res = yield
        print('%s 正在吃包子 %s' %(name, res))

'''
c = consumer('jj')
next(c)
c.send('A') # 执行next（）功能，并且传递一个结果值
'''

def producer(name):
    c1 = consumer('xx')
    c2 = consumer('oo')
    next(c1)
    next(c2)
    print('prepare')

    for i in range(5):
        time.sleep(1)
        print(name,'做了2个包子')
        c1.send('A')
        c2.send('B')

producer('jj')