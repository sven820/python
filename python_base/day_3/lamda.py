__author__ = "JJ.sven"

import functools

# 匿名函数

print(lambda x: x + 1)

calc = lambda x, y: x + y
print(calc(1, 2))

# lambda 匿名函数
# filter 根据条件（函数）过滤
filter_list = filter(lambda x: x > 5, list(range(10)))
for i in filter_list:
    print(i)

# map 根据条件，构造新的序列
map_list = map(lambda x, y, z: x * y * z, range(10), range(10), range(10))
for i in map_list:
    print(i)

# reduce 累积算法 把结果继续和序列的下一个元素做累积计算
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
res = functools.reduce(lambda x, y: x+y, range(10))
print(res)

# sort 根据key返回的结果排序
res = sorted([1, -3, 2, 5, 4], key=lambda x: abs(x), reverse=False)
print(res)
