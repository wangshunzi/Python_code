
# -----------------------------------------几个监听对象生命周期的方法-----------------------
# class Person:
#     # def __new__(cls, *args, **kwargs):
#     #     print("新建了一个对象, 但是, 被我拦截了")
#     def __init__(self):
#         print("初始化方法")
#         self.name = "sz"
#
#     def __del__(self):
#         print("这个对象被释放了")
#     pass
#
# p = Person()
# del p
# print(p)
# print(p.name)

# --------------------------------监听对象生命周期的方法-小案例-----------------------

# Person, 打印一下, 当前这个时刻, 由Person类, 产生的实例, 由多少个
# 创建了一个实例, 计数 + 1, 如果, 删除了一个实例, 计数 - 1

class Person:
    __personCount = 0
    def __init__(self):
        print("计数 + 1")
        Person.__personCount += 1

    def __del__(self):
        print("计数 - 1")
        self.__class__.__personCount -= 1

    @classmethod
    def log(cls):
        print("当前的人的个数是%d个" % cls.__personCount)

Person.personCount = 100
p = Person()
p2 = Person()
Person.log()
del p
del p2
Person.log()


