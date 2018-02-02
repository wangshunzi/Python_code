#_*_encoding:utf-8_*_
# class Person:
#     pass
#
# p = Person()
# print(p)
# # print(id(p))
# # print(hex(id(p)))
#
# p2 = Person()
#
# print(id(p), id(p2))
#
#
# # 1, 2, 3
#
# num1 = 2
# num2 = 2
# print(id(num1), id(num2))
# p.name = "sz"

# ---------------------------引用计数器--------------------------------

# import sys
#
# class Person:
#     pass
#
# p1 = Person() # 1
#
# print(sys.getrefcount(p1))
#
# p2 = p1 # 2
#
# print(sys.getrefcount(p1))
#
# del p2 # 1
# print(sys.getrefcount(p1))
#
# del p1
# print(sys.getrefcount(p1))



# ---------------------------引用计数器+1 -1 的场景举例--------------------------------

# import sys
#
# class Person:
#     pass
#
# p_xxx = Person() # 1
#
# print(sys.getrefcount(p_xxx))


# def log(obj):
#     print(sys.getrefcount(obj))
#
# log(p_xxx)
#
#
# for attr in dir(log):
#     print attr, getattr(log, attr)


# ---------------------------引用计数器机制-特殊场景-循环引用问题--------------------------------

# 内存管理机制 = 引用计数器机制 + 垃圾回收机制
# 当一个对象, 如果被引用 + 1, 删除一个引用 : -1 0: 被自动释放
# 循环引用
# objgraph
# objgraph.count() 可以查看, 垃圾回收器, 跟踪的对象个数

# import objgraph
#
# class Person:
#     pass
#
#
# class Dog:
#     pass
#
# p = Person()
# d = Dog()
#
# print(objgraph.count("Person"))
# print(objgraph.count("Dog"))
#
# p.pet = d
# d.master = p
#
# # 删除 p, d之后, 对应的对象是否被释放掉
# del p
# del d
#
# print(objgraph.count("Person"))
# print(objgraph.count("Dog"))




# ---------------------------------垃圾回收机制-如何检测"循环引用"---------------------------------------

#
# class Person:
#     pass
#
# p = Person()
# l = [p]
# t = (p)
# # p.pet = Dog()
#
#
#
# num = True
# num.age = 10


# ---------------------------------垃圾回收机制-分代回收---------------------------------------


# import gc
#
# print(gc.get_threshold())
# gc.set_threshold(200, 5, 5)
#
# print(gc.get_threshold())


# ---------------------------------垃圾回收机制-触发时机---------------------------------------


# 自动回收
#
# import gc
#
# gc.disable()
# print(gc.isenabled())
#
# gc.enable()
#
# print(gc.isenabled())
#
# print(gc.get_threshold())
# gc.set_threshold(1000, 15, 5)


# 手动回收
# import objgraph
# import gc
# gc.disable()
# class Person:
#     pass
#
# class Dog:
#     pass
#
# p = Person()
# d = Dog()
#
# p.pet = d
# d.master = p
#
#
# del p
# del d
#
# gc.collect()
#
# print(objgraph.count("Person"))
# print(objgraph.count("Dog"))


# -----------------------------------循环引用-细节问题(版本兼容方案)---------------------------------------
import objgraph
import gc
import weakref
# import weakref

# 1. 定义了两个类
class Person:
    def __del__(self):
        print("Person对象, 被释放了")
    pass

class Dog:
    def __del__(self):
        print("Dog对象, 被释放了")
    pass

# 2. 根据这两个类, 创建出两个实例对象
p = Person()
d = Dog()

# 3. 让两个实例对象之间互相引用, 造成循环引用
# p.pets = {"dog":  weakref.ref(d1), "cat":  weakref.ref(c1)}
# weakref.WeakValueDictionary({"dog": d1, "cat": c1})
# p.pet = d
# d.master = weakref.ref(p)
# d.master = p

# 4. 尝试删除可到达引用之后, 测试真实对象是否有被回收
# p.pet = None
del p
del d

# 5. 通过"引用计数机制"无法回收; 需要借助"垃圾回收机制"进行回收
# gc.collect()

print(objgraph.count("Person"))
print(objgraph.count("Dog"))

