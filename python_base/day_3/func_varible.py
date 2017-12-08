__author__ = "JJ.sven"

name = 'jj'
a = 2

def test():
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
