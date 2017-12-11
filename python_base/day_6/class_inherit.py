__author__ = "JJ.sven"

import types

class Animal:
    def __init__(self):
        self.age = 0
        self.height = 0
        self.weight = 0
        self.name = 0

    def walk(self, step = 1):
        print('walk %d step' % (step))


class Person(Animal):
    def __init__(self):
        pass

animal = Animal()
person = Person()

person.walk()
'''判读类型'''
'''type'''
def func():
    pass
print(type(123) == int)
print(type(func) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x + 1) == types.LambdaType)
print(type(x for x in range(10)) == types.GeneratorType)

print(type(person) == Person)
print(type(person) == Animal)

'''isinstance'''
print(isinstance(123, int))
print(isinstance(person, Person), isinstance(person, Animal))

print(isinstance([], (list, tuple)))

'''“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，
    那它就可以被看做是鸭子'''