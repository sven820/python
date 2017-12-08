__author__ = "JJ.sven"


# 默认参数放在最后
def test(x, y, z=1):
    print(x, y, z)


# 关键字参数一定要在位置参数之后，关键字参数可以不管顺序
test(2, 4, 6)
test(2, z=8, y=9)
test(2, y=10)


# 可变参数(位置参数)
def test2(x, *args, y):
    print(x)
    print(args)
    pass


test2(1, 2, 3, 4, y=3)


# 关键字参数
def test3(**kwargs):
    print(kwargs)


test3(name='jj', age='18')


# 命名关键字参数, 限制了关键字参数的名字
def test3_1(x, *, name, age=18):
    print(x, name, age)
    pass


# 命名关键字参数 调用必须要有关键字=xx的形式
test3_1(1, name='jj')


# 如果有可变参数，则可以省略*，直接写在可变参数后面
def test3_2(*args, name, age=18):
    print(args)
    print(name, age)


test3_2(1, name='jj')


def test4(x, y=1, *args, **kwargs):
    print(x, y)
    print(args)
    print(kwargs)
    pass


test4(1, 2, 3, name='jj')
