# class Person(object):
#     def __init__(self):
#         self.__age = 18
#
#     # 主要作用就是, 可以以使用属性的方式, 来使用这个方法
#     @property
#     def age(self):
#         return self.__age
#
#
# p1 = Person()
# # print(p1.__age)
# # print(p1.getAge())
# #
# #
# # p1.age = 1
# # p1._Person__age = 999
# p1.__dict__["_Person__age"] = 999
# print(p1.age)
# # p1.age = 10
#
#
# # p1.__age = 999
# # print(p1.__dict__)
#
#


class Person:
    # 当我们通过 "实例.属性 = 值", 给一个实例增加一个属性, 或者说, 修改一下属性值的时候, 都会调用这个方法
    # 在这个方法内部, 才会真正的把, 这个属性, 以及对应的数据, 给存储到__dict__字典里面
    def __setattr__(self, key, value):
        print(key, value)

        # 1. 判定, key, 是否是我们要设置的只读属性的名称
        if key == "age" and key in self.__dict__.keys():
            print("这个属性是只读属性, 不能设置数据")
        # 2. 如果说不是, 只读属性的名称, 真正的给它添加到这个实例里面去
        else:
            # self.key = value
            self.__dict__[key] = value
p1 = Person()
p1.age = 18
# p1.name = "sz"
# print(p1.age)
print(p1.age)


p1.age = 999
print(p1.age)

print(p1.__dict__)