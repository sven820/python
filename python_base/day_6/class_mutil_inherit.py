__author__ = "JJ.sven"

class Animal:
    '''多继承
       在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。
       但是，如果需要“混入”额外的功能，通过多重继承就可以实现，
       比如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn。

       设计的时候这种额外功能的可以格式名为*MixIn,表示额外功能，这样原有的继承结构也不会被破坏
    '''

    def eat(self):
        print('eat eat')

class Fly:

    def fly(self):
        print('fly fly')

class Dog(Animal):


    def bark(self):
        print('wang wang')


class Bird(Animal, Fly):
    pass


bird = Bird()
bird.eat()
bird.fly()