__author__ = "JJ.sven"

import functools

# 本质是函数，为其它函数添加附加功能

# 不带参数的装饰器
'''
def dec(fun):
    @functools.wraps(fun) 
    def wrapper(*args, **kwargs):
        res = fun(*args, **kwargs)
        print('handle dec')
        return res
    return wrapper;

@dec   # test = dec(test)
def test():
    print('handle test')

@dec
def test1(str):
    print('handle test1', str)

test()
test1('value')
'''


# 带参数的装饰器
def dec(type):
    def fun_wraper(fun):
        '''
        因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。

不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的
        '''

        @functools.wraps(fun)
        def wrapper(*args, **kwargs):
            print(type)
            res = fun(*args, **kwargs)
            print('handle dec')
            return res

        return wrapper;

    return fun_wraper;


@dec(type='local')  # test = dec('local')(test)
def test():
    print('handle test')
    return 'return test'


@dec(type='server')
def test1(str):
    print('handle test1', str)
    return 'return test1'


print(test())
# print(test1('value'))
