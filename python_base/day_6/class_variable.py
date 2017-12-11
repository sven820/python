__author__ = "JJ.sven"

from types import MethodType


class MyClass:
    '''类的相关注意点'''

    '''类变量，类和实例都能访问，访问优先级低于实例， 但一般不要和实例重名'''
    name = '类变量'

    '''限制类的属性, 只对当前类起作用，子类不起作用'''

    # __slots__ = ('name', 'age')

    def __init__(self, type):
        '''实例变量， 外部也可以动态添加或删除实例变量'''

        '''public'''
        self.type = type
        self.num = 0
        '''privite，带2个__,
           内部会把__kind 处理成_MyClass__kind,
           所以实际上也能访问，只是解释器把变量换了名称'''
        self.__kind = 0
        '''privite，带1个_, 是我们自己约定的private的变量，告诉外边最好不要访问或修改
           如果要修改访问，则田间set， get方法形式暴露给外面
           通常用@property来对参数检查'''
        self._age = 10

        '''-------------'''
        self.name = 'jj'

        pass

    def func1(self):
        pass

    '''----------set & get 普通写法 ------------'''

    def set_age(self, age):
        self._age = age

    def get_age(self):
        return self._age

    '''----------set & get @property ------------'''
    @property
    def score(self):
        if self._score > 60:
            print('及格')
        else:
            print('不及格')
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    @score.deleter
    def score(self):
        del self._score


cl = MyClass(1)
print(cl)
print(cl.type, cl.num)
print(cl._MyClass__kind)  # print(cl.__kind)
print(cl._age)
print(cl.name, MyClass.name)

cl.score = 50
print(cl.score)

'''动态绑定属性'''
# cl.cus = 'cus'
# print(cl.cus)
# del cl.cus
# print(cl.cus)
'''对象 动态绑定方法，只对对象有用'''
# def func2(self):
#     print('cus func2')
# cl.func2 = MethodType(func2, cl)
# cl.func2()
'''类 动态绑定方法，对所有对象有用'''
# def func3(self):
#     print('cus func3')
# MyClass.func3 = func3
# cl.func3()

'''dir(obj), 获取属性和方法'''
'''hasattr, setattr, getattr'''
# print('----hasattr, setattr, getattr----')
# print(hasattr(cl, 'func1'))
# print(hasattr(cl, 'num'))
#
# print(getattr(cl, 'num2', 10))
# setattr(cl, 'num2', 30)
# print(cl.num2)
