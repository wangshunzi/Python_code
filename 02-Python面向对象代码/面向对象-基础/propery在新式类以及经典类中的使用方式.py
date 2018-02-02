# _*_ encoding:utf-8 _*_
# class Person(object):
#     def __init__(self):
#         self.__age = 18
#
#
#     def get_age(self):
#         print("----, get")
#         return self.__age
#
#     def set_age(self, value):
#         print("----, set")
#         self.__age = value
#
#
#     age = property(get_age, set_age)
#
#
# p = Person()
# print(p.age)
#
# p.age = 90
# print(p.age)
#
# print(p.__dict__)


# 第二种使用方式

# class Person(object):
#     def __init__(self):
#         self.__age = 18
#
#     @property
#     def age(self):
#         print("----- get")
#         return self.__age
#
#     @age.setter
#     def age(self, value):
#         print("----- set")
#         self.__age = value
#
# p = Person()
# print(p.age)
#
# p.age = 10
# print(p.age)

# -------------------------------property在经典类中的使用---------------------------------------

#
# class Person:
#     def __init__(self):
#         self.__age = 18
#
#
#     def get_age(self):
#         print("----, get")
#         return self.__age
#
#     def set_age(self, value):
#         print("----, set")
#         self.__age = value
#
#
#     age = property(get_age, set_age)
#
#
# p = Person()
# print p.age
#
# p.age = 19
# print p.age
#
# print p.__dict__




class Person:
    def __init__(self):
        self.__age = 18

    @property
    def age(self):
        print "-----get"
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

p = Person()
# print p.age

p.age = 19
print p.age
print p.__dict__







