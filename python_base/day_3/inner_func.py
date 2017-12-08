__author__ = "JJ.sven"

import functools

# 元素全部为真则为真，作用可迭代对象
print(all([1, 2, 0]))
# 元素任意为真则为真，作用可迭代对象
print(all([1, 2, 0]))
# 将对象变为字符串
print(ascii([1, 2, 'jjjj']))
# 十进制转二进制
print(bin(12))
# hex 转16进制
print(hex(20))
# oct 8进制
print(oct(20))
# power 幂次方
print(pow(2, 3))
#
print(bool([1, 0]))
# 转byte
print(bytes('jin xiaofei', encoding='utf-8'))
b = bytearray('jin xiao fei', encoding='utf-8') #可变二进制数组
b[0] = 99
print(b)
# ascii =》str
print([chr(99)])
print([ord('A')])
# callable 是否可以调用
def test():
    pass
print(callable(test))

# compile 编译代码
# exec
code = "print('jin xiaofei')"
py_obj = compile(code, '', 'exec')
exec(py_obj)
exec(code)

# eval 计算算术表达式
print(eval('1 + 1'))

# complex 复数

#dir 查看内部方法
print(dir([]))

# divmod 返回整数结果，余数
print(divmod(5, 2))

# enumerate
for i in enumerate('jjjj'):
    print(i)

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

# frozenset 不可变集合

# globals 整个程序的全局变量
print(globals())
# 局部所有变量
print(locals())

# hash() 散列
print(hash('jinxiaofei'))

# max， min
print(max('jinxiaofei'), min('jinxiaofei'))

# 作用迭代 next()

# open file

# repr 把对象转成字符串描述
print(repr([]))

# reversed()

# round 保留两位
print(round(1.33456, 2))

# slice 切片

# 排序 sorted()

# vars（）对象所有属性名

# zip
a = [1, 2, 3, 4]
b = ['a', 'b', 'c', 'd', 'f']
for i in zip(a, b):
    print(i)
