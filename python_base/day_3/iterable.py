__author__ = "JJ.sven"

from collections import Iterable
from collections import Iterator

# 迭代器 Iterator
'''
    生成器 generator都是迭代器，所有能被next（）调用的都是迭代器
'''

# 可迭代的 Iterable
'''
    迭代器 表示一个数据流
    arr, dict, set, str 不能表示数据流，所以不是迭代器，但for循环,其实是用iter()，将其改造为迭代器
'''

itor = (i * 2  for i in range(10))

def fib(n):
    index, a, b = 0, 0, 1
    while index < n:
        yield b
        a, b = b, a + b
        index += 1

l = [1, 2, 3, 4]
l_iteraor = iter(l)

print(isinstance(itor, Iterator)) # T
print(isinstance(itor, Iterable)) # T

print(isinstance(fib(10), Iterator)) # T
print(isinstance(fib(10), Iterable)) # T

print(isinstance(l, Iterator)) # F
print(isinstance(l, Iterable)) # T

print(isinstance(l_iteraor, Iterator)) # T
print(isinstance(l_iteraor, Iterable)) # T






