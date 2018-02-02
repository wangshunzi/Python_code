
# --------------------------------------多态-------------------------------------

import abc

class Animal(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def jiao(self):
        pass

    @abc.abstractclassmethod
    def test(cls):
        pass

class Dog(Animal):
    def jiao(self):
        print("汪汪汪")

    @classmethod
    def test(cls):
        print("xxxxx")
    pass

class Cat(Animal):
    def jiao(self):
        print("喵喵喵")


def test(obj):
    obj.jiao()

d = Dog()
d.jiao()
d.test()

# a = Animal()
# a.jiao()
# d = Dog()
# d.hehe()
# c = Cat()
# test(d)
























