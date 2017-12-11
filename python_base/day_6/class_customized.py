__author__ = "JJ.sven"


class CustomizedClass(object):
    '''定制类 这里对应__doc__属性'''

    def __init__(self):
        self.name = 'll'
        pass

    '''print'''

    def __str__(self):
        return 'CustomizedClass'
        pass

    '''控制台调试'''

    def __repr__(self):
        return 'CustomizedClass'
        pass

    # __repr__ = __str__

    '''len()'''

    def __len__(self):
        pass

    '''for in'''

    def __iter__(self):
        pass

    ''' list[2] '''

    def __getitem__(self, item):
        '''item => key | num | slice'''
        pass

    '''dic[key] = value'''

    def __setitem__(self, key, value):
        pass

    def __delitem__(self, key):
        pass

    def __getattr__(self, item):
        '''如果没重写__setattr__， 则只调用没有的属性时才会调用getattr方法
           如果同时重写了如果没重写__setattr__，调用已有属性也会调用getattr
        '''
        print('getattr', item)

    # def __setattr__(self, key, value):
    #     print('setattr', key, value)

    def __call__(self, *args, **kwargs):
        '''对象可直接调用'''
        print(args, kwargs)


c = CustomizedClass()
print(c.name)

if callable(c):
    c('18', name='jj')

'''__getattr__实现链式抵用'''
class Chain():
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


print(Chain().user.timeline.list)

'''__doc__ 类注释'''
print(CustomizedClass.__doc__)
'''__module__ 输出模块'''
print(c.__module__)
'''__class__ 类名 路径'''
print(c.__class__)
'''__dict__'''
print(CustomizedClass.__dict__)
print(c.__dict__)
'''__str__'''
print(c)
