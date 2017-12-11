__author__ = "JJ.sven"

'''经典类'''
# class Demo:
'''新式类, 新式类才有super (但经典类好像也能用。。。)'''


class Demo(object):
    '''test'''

    '''构造函数'''
    name = 'lei bianliang'

    def __init__(self):
        # print('__init__')
        self.name = 'jj'
        pass

    '''析构函数'''

    def __del__(self):
        # print('__del__')
        pass

    def func1(self):
        print('demo func 1')

    '''可继承，可重写，不依赖对象
        self 是类 class， 只能访问类变量
    '''
    @classmethod
    def classMethod(self, obj):
        print('class method', obj, self.name)
        pass

    '''可继承的，但不能被重写，不依赖对象'''
    @staticmethod
    def staticFunc():
        print('static method')


class SubDemo(Demo):
    def func1(self):
        super(SubDemo, self).func1()
        print('SubDemo func 1')


s = SubDemo()
s.func1()

d = Demo()
Demo.classMethod('jj')

# d.staticFunc()
# s.staticFunc()

'''关系映射'''
if hasattr(d, 'func1'):
    getattr(d, 'func1')()

def mapFunc():
    print('map func')
setattr(d, 'mapFunc', mapFunc)
d.mapFunc()

setattr(d, 'map_veriable', 'jj')
print(d.map_veriable)

if hasattr(d, 'map_veriable'):
    print('exist',d.map_veriable)
    delattr(d, 'map_veriable')
