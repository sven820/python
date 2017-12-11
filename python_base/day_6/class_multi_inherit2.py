__author__ = "JJ.sven"

''' 多继承顺序问题
    
    python2  
   新式类 继承为广度优先
   旧式类 继承为深度优先
    
    python3
   都是统一按广度优先
'''

class A(object):
    def __init__(self):
        pass


class B(A):
    def __init__(self):
        pass


class C(A):
    def __init__(self):
        pass


class D(B, C):
    def __init__(self):
        pass

