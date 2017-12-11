__author__ = "JJ.sven"


class Cls(object):

    pass


'''动态定义和创建类
    type('Cls name', (super cls name,), {'func': func})
'''


def func(self):
    print('func')


'''Foo type类的类对象'''
Foo = type('Foo', (object,), {'func': func})
f = Foo()
f.func()


''' 自定义元类 http://stackoverflow.com/questions/100003/what-is-a-metaclass-in-python

    类中有一个属性 __metaclass__，其用来表示该类由 谁 来实例化创建，
    所以，我们可以为 __metaclass__ 设置一个type类的派生类，
    从而查看 类 创建的过程
'''

# '''
class MyType(type):
    def __init__(self, *args, **kwargs):
        print("Mytype __init__", *args, **kwargs)

    def __call__(self, *args, **kwargs):
        print("Mytype __call__", *args, **kwargs)
        obj = self.__new__(self, *args, **kwargs)
        print("obj ", obj, *args, **kwargs)
        print(self, '==========', type(self))
        self.__init__(obj, *args, **kwargs)
        return obj

    def __new__(cls, *args, **kwargs):
        print("Mytype __new__", *args, **kwargs)
        return type.__new__(cls, *args, **kwargs)


class Foo(object, metaclass=MyType):
    def __init__(self, name):
        self.name = name

        print("Foo __init__")

    def __new__(cls, *args, **kwargs):
        print("Foo __new__", cls, *args, **kwargs)
        return object.__new__(cls)


f = Foo("Alex")
print("f", f)
print("fname", f.name)
# '''
