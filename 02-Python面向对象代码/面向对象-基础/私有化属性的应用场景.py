class Person:

    # 主要作用, 当我们创建好一个实例对象之后, 会自动的调用这个方法, 来初始化这个对象
    def __init__(self):
        self.__age = 18

    def setAge(self, value):
        if isinstance(value, int) and 0 < value < 200:
            self.__age = value
        else:
            print("你输入的数据有问题, 请重新输入")

    def getAge(self):
        return self.__age

p1 = Person()
# p1.__age = -10
# print(p1._Person__age)
p1.setAge("abc")

# print(p1._Person__age)

print(p1.getAge())

p2 = Person()


p3 = Person()

# print(p1.age)
# print(p2.age)
# print(p3.age)
# print(p1.__dict__)

# class_

__xx__