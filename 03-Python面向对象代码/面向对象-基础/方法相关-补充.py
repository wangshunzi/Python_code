# _*_ encoding:utf-8 _*_
# class Person:
#     __age = 18
#
#     def __run(self):
#         print("pao")
#
#     def _Person__run(self):
#         print("xxx")
#
#
# p = Person()
# p._Person__run()
#
# print(Person.__dict__)


# class Person:
#     def __init__(self, n, a):
#         self.name = n
#         self.age = a
#
#     def __str__(self):
#         return "这个人的姓名是%s, 这个人的年龄是:%s" % (self.name, self.age)
#
# p1 = Person("sz", 18)
# # print(p1.name)
# # print(p1.age)
# print(p1)
#
# p2 = Person("zhangsan", 19)
# # print(p2.name)
# # print(p2.age)
# print(p2)
#
# s = str(p1)
# print(s, type(s))

# class Person:
#     def __init__(self, n, a):
#         self.name = n
#         self.age = a
#
#     def __str__(self):
#         return "这个人的姓名是%s, 这个人的年龄是:%s" % (self.name, self.age)
#
#     def __repr__(self):
#         return "reprxxxxx"
#
# p1 = Person("sz", 18)
# # print(p1.name)
# # print(p1.age)
# print(p1)
#
# p2 = Person("zhangsan", 19)
# # print(p2.name)
# # print(p2.age)
# print(p2)
#
# s = str(p1)
# print(s, type(s))
#
# print(repr(p1))

# import datetime
#
# t = datetime.datetime.now()
# print(t)
# print(repr(t))
#
# tmp = repr(t)
#
# result = eval(tmp)
# print(result)


# ----------------------------__call__方法------------------------------------


# class Person:
#     def __call__(self, *args, **kwargs):
#         print("xxx", args, kwargs)
#         pass
#
# p = Person()
#
# p(123, 456, name="sz")



# 创建很多个画笔, 画笔的类型(钢笔, 铅笔), 画笔的颜色(红, 黄色, 青色, 绿色)

# print("创建了一个%s这个类型的画笔, 它是%s颜色" % ("钢笔", "红色"))
# print("创建了一个%s这个类型的画笔, 它是%s颜色" % ("钢笔", "黄色"))
# print("创建了一个%s这个类型的画笔, 它是%s颜色" % ("钢笔", "青色"))
# print("创建了一个%s这个类型的画笔, 它是%s颜色" % ("钢笔", "绿色"))
# print("创建了一个%s这个类型的画笔, 它是%s颜色" % ("钢笔", "橘色"))


# def createPen(p_color, p_type):
#     print("创建了一个%s这个类型的画笔, 它是%s颜色" % (p_type, p_color))
#
#
# # createPen("钢笔", "红色")
# # createPen("钢笔", "绿色")
# # createPen("钢笔", "黄色")
#
# import functools
#
# gangbiFunc = functools.partial(createPen, p_type="钢笔")
#
# gangbiFunc("红色")
# gangbiFunc("黄色")
# gangbiFunc("绿色")

#
# class PenFactory:
#
#     def __init__(self, p_type):
#         self.p_type = p_type
#
#     def __call__(self, p_color):
#         print("创建了一个%s这个类型的画笔, 它是%s颜色" % (self.p_type, p_color))
#
# # gangbiF = PenFactory("钢笔")
# # gangbiF("红色")
# # gangbiF("绿色")
# # gangbiF("黄色")
#
#
# qianbiF = PenFactory("铅笔")
# qianbiF("红色")
# qianbiF("绿色")
# qianbiF("黄色")

# ----------------------------索引操作------------------------------------


# class Person:
#     def __init__(self):
#         self.cache = {}
#
#     def __setitem__(self, key, value):
#         # print("setitem", key, value)
#         self.cache[key] = value
#
#     def __getitem__(self, item):
#         # print("getitem", item)
#         return self.cache[item]
#
#     def __delitem__(self, key):
#         # print("delitem", key)
#         del self.cache[key]
#
# p = Person()
# p["name"] = "sz"
#
# print(p["name"])
#
# del p["name"]
#
# # print(p["name"])
# print(p.cache)


# ----------------------------切片操作------------------------------------


# l = [1, 2, 3, 4, 5]
# # print(l[3])
# print(l[1: 4: 2])


#
# class Person:
#
#     def __init__(self):
#         self.items = [1, 2, 3, 4, 5, 6, 7, 8]
#
#     def __setitem__(self, key, value):
#         # print(key, value)
#         # print(key.start)
#         # print(key.stop)
#         # print(key.step)
#         # print(value)
#         # self.items[key] = value
#         if isinstance(key, slice):
#             self.items[key.start: key.stop: key.step] = value
#
#     def __getitem__(self, item):
#         print("getitem", item)
#
#     def __delitem__(self, key):
#         print("delitem", key)
#
# p = Person()
# p[0: 4: 2] = ["a", "b"]
# print(p.items)
# slice

# p[0: 5: 2]
# del p[0: 5: 2]

# ----------------------------比较操作------------------------------------

# class Person:
#     def __init__(self, age, height):
#         self.age = age
#         self.height = height
#     # == != > >= < <=
#
#     def __eq__(self, other):
#         print("eq")
#         return self.age == other.age

# def __ne__(self, other):
#     pass
#
# def __gt__(self, other):
#     pass
#
# def __ge__(self, other):
#     pass
#
# def __lt__(self, other):
#     # print("lt")
#     print(self.age)
#     print(other.age)
#     return self.age < other.age
#
# def __le__(self, other):
#     pass


# p1 = Person(18, 190)
# p2 = Person(19, 190)
# print(p1 < p2)
# print(p1 <= p2) # p2 < p1
# print(p1 == p2)
# print(p1 != p2)
# print(p1 <= p2)


# ----------------------------比较操作-补充------------------------------------

# import functools
#
#
# @functools.total_ordering
# class Person:
#     def __lt__(self, other):
#         print("lt")
#         # pass
#         return False
#
#     def __eq__(self, other):
#         print("eq")
#         pass
#
#     # def __le__(self, other):
#     #     print("le")
#
# p1 = Person()
# p2 = Person()
#
# print(p1 <= p2)
#
# print(Person.__dict__)


# ----------------------------上下文环境的布尔值------------------------------------

# class Person:
#     def __init__(self):
#         self.age = 20
#
#     def __bool__(self):
#         return self.age >= 18
#     pass
#
# p = Person()
#
#
# if p:
#     print("xx")


# ----------------------------遍历操作------------------------------------


# class Person:
#     def __init__(self):
#         self.result = 1
#
#     def __getitem__(self, item):
#         self.result += 1
#         if self.result >= 6:
#             raise StopIteration("停止遍历")
#
#         return self.result
#     pass
#
# p = Person()
#
# for i in p:
#     print(i)


# 方式2
# class Person:
#     def __init__(self):
#         self.result = 1
#
#     def __iter__(self):
#         print("iter")
#         self.result = 1
#         # return iter([1, 2, 3, 4, 5])
#         return self
#
#     def __next__(self):
#         self.result += 1
#         if self.result >= 6:
#             raise StopIteration("停止遍历")
#         return self.result
#
# p = Person()
#
# # for i in p:
# #     print(i)
#
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))

# result = next(p)
# while result:
#     print(result)
#     result = next(p)



# ----------------------------恢复迭代器初始值------------------------------------


# class Person:
#     def __init__(self):
#         self.age = 1
#
#
#     def __getitem__(self, item):
#         return 1
# def __iter__(self):
#     self.age = 1
#     return self
#
# def __next__(self):
#     self.age += 1
#     if self.age >= 6:
#         raise StopIteration("stop")
#
#     return self.age

# next()
# p = Person()

# for i in p:
#     print(i)
# print(p.age)
# for i in p:
#     print(i)

# import collections
# print(isinstance(p, collections.Iterator))
# print(isinstance(p, collections.Iterable))


# ----------------------------iter函数的使用------------------------------------


#
# class Person:
#     def __init__(self):
#         self.age = 1

    # def __getitem__(self, item):
    #     self.age += 1
    #     if self.age >= 6:
    #         raise StopIteration("stop")
    #     return self.age

    # def __iter__(self):
    #     self.age = 1
    #     return self

    # def __next__(self):
    #     self.age += 1
    #     if self.age >= 6:
    #         raise StopIteration("stop")
    #     return self.age

#     def __call__(self, *args, **kwargs):
#         self.age += 1
#         if self.age >= 6:
#             raise StopIteration("stop")
#         return self.age
# p = Person()


# pt = iter(p)
# pt = iter(p.__next__, 4)
# pt = iter(p, 4)

# print(pt is p)
#
# for i in pt:
#     print(i)

# l = [1, 2, 3]
# lt = iter(l)
# print(lt)



# ----------------------------描述器-定义方式1------------------------------------


# class Person:
#     def __init__(self):
#         self.__age = 10
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, value):
#         if value < 0:
#             value = 0
#         self.__age = value
#
#     @age.deleter
#     def age(self):
#         print("del age")
#         del self.__age

    # age = property(get_age, set_age, del_age)
    # name = "sz"

# p = Person()
# p.age = 19
# del p.age
# print(p.age)
# p.age = 19
# print(p.age)
# del p.age
# print(p.age)
# p.set_age(-10)
# print(p.get_age())
# p.del_age()
# print(p.get_age())
# p.age = 10

# help(Person)







# ----------------------------描述器-定义方式2------------------------------------


# class Age:
#     def __get__(self, instance, owner):
#         print("get")
#
#     def __set__(self, instance, value):
#         print("set")
#
#     def __delete__(self, instance):
#         print("delete")
#
# class Person:
#     age = Age()
    # def __init__(self):
    #     self.__age = 10
    #
    # # @property
    # def get_age(self):
    #     return self.__age
    #
    # # @age.setter
    # def set_age(self, value):
    #     if value < 0:
    #         value = 0
    #     self.__age = value
    #
    # # @age.deleter
    # def del_age(self):
    #     print("del age")
    #     del self.__age
    #
    # age = property(get_age, set_age, del_age)

# p = Person()
# p.age = 10
# print(p.age)
# del p.age


# ----------------------------描述器-调用细节------------------------------------


# class Age(object):
#     def __get__(self, instance, owner):
#         print("get")
#
#     def __set__(self, instance, value):
#         print("set")
#
#     def __delete__(self, instance):
#         print("delete")
#
#
# class Person(object):
#     age = Age()
#     def __getattribute__(self, item):
#         print "xxxxx"
#
#
# p = Person()
#
# p.age = 10
# print(p.age)
# del p.age

# print(Person.age)
# Person.age = 19
# del Person.age


# ----------------------------描述器-和实例属性同名时, 操作优先级------------------------------------

# 资料描述器 get set
# 非资料描述器 仅仅实现了 get 方法, 那么他就是一个非资料描述器
# 资料描述器 > 实例属性 > 非资料描述器
# class Age(object):
#     def __get__(self, instance, owner):
#         print("get")
#
#     def __set__(self, instance, value):
#         print("set")
#
#     def __delete__(self, instance):
#         print("delete")
#
#
# class Person(object):
#     age = Age()
#     def __init__(self):
#         self.age = 10
#
# p = Person()
#
# p.age = 10
# print(p.age)
# # del p.age
#
# print(p.__dict__)




# ----------------------------描述器-值的存储问题------------------------------------
#
# class Person:
#     def __init__(self):
#         self.__age = 10
#
#     def get_age(self):
#         return self.__age
#
#     def set_age(self, value):
#         if value < 0:
#             value = 0
#         self.__age = value
#
#     def del_age(self):
#         print("del age")
#         del self.__age
#
#     age = property(get_age, set_age, del_age)
#
# p = Person()
# p.age = 10
# print(p.age)
# del p.age



# class Age(object):
#     def __get__(self, instance, owner):
#         print("get")
#         return instance.v
#
#     def __set__(self, instance, value):
#         print("set", self, instance, value)
#         instance.v = value
#
#     def __delete__(self, instance):
#         print("delete")
#         del instance.v
#
#
# class Person(object):
#     age = Age()
#
#
# p = Person()
# p.age = 10
# print(p.age)
# # del p.age
#
# p2 = Person()
# p2.age = 11
# print(p2.age)
# print(p.age)

# ----------------------------使用类, 实现装饰器------------------------------------


# def check(func):
#     def inner():
#         print("登录验证")
#         func()
#     return inner
class check:
    def __init__(self, func):
        self.f = func

    def __call__(self, *args, **kwargs):
        print("登录验证")
        self.f()

@check
def fashuoshuo():
    print("发说说")
# fashuoshuo = check(fashuoshuo)

fashuoshuo()

x = "abc"
y = [x]
z = [x, y]
import objgraph
# objgraph.show_refs(y, filename='test.png')
objgraph.show_refs(z, filename="test.png")
