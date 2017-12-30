__author__ = "JJ.sven"

name = 'jj'
a = 2

def test():
    '''

    :return:
    '''

    '''global 如果外部只是想访问全局变量，则可直接访问，
       如果要修改，就需要使用global关键字申明'''
    global name
    name = 'xx'

    print(name)

    name = 'oo'
    print(name)

    # 表示age为全局变量，但不要这么用，逻辑不清了
    global age
    age = 12
    print(age)

    pass


test()
print(name)
print(age)
