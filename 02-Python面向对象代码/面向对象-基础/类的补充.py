


#
# num = 10
#
# print(num.__class__)
#
#
# s = "abc"
# print(s.__class__)
#
#
# class Person:
#     pass
#
# p = Person()
# print(p.__class__)
#
#
# print("-"*20)
#
#
# print(int.__class__)
# # print(num.__class__.__class__)
#
# print(str.__class__)
#
# print(Person.__class__)
# print(Person.__class__.__class__)
# print(type.__class__)


# -----------------------------类的创建方式---------------------------




# class Person:
#     count = 0
#     def run(self):
#         pass



# num = 10
# print(type(num))

# def run(self):
#     print("---", self)
#
# xxx = type("Dog",(),{"count": 0, "run": run})
# print(xxx)
#
# print(xxx.__dict__)

# d = xxx()
# print(d)
#
# d.run()



# -----------------------------类的创建流程------------------

class Test():
    pass
__metaclass__ = Test

class Animal:
    # __metaclass__ = Test
    pass


class Person(Animal):
    # __metaclass__ = Test
    pass

#
# class Dog(Animal):
#     __metaclass__ = xxx
#     pass

# print(Person.__metaclass__)




















