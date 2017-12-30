__author__ = "JJ.sven"

name = 'xx'


def fun1():
    name = 'jj'

    def fun2():
        print(name)

    return fun2


t = fun1()
t()
