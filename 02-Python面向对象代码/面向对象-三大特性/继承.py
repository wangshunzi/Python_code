# _*_ encoding:utf-8 _*_
# class Animal:
#     pass
#
# class xxx:
#     pass
#
# class Dog(Animal, xxx):
#     pass
#
#
# d = Dog()
#
# print(d.__class__)
# print(Dog.__class__)
# print(type.__class__)
# print(object.__class__)

# print(Dog.__bases__)
# print(Animal.__bases__)
# # object
#
# print(int.__bases__)
# print(float.__bases__)
# print(bool.__bases__)
#
# type


# ---------------------------------------继承-资源---------------------------------------------



# class Animal:
#     # 属性 和方法
#     # 设置不同权限的属性和方法, 继承当中, 进行测试
#     # 在子类当中, 能否访问到这些资源
#     a = 1
#     _b = 2
#     __c = 3
#
#     def t1(self):
#         print("t1")
#
#     def _t2(self):
#         print("t2")
#
#     def __t3(self):
#         print("t3")
#
#     def __init__(self):
#         print("init, Animal")
#
#
# class Person(Animal):
#     def test(self):
#         print(id(self.a))
#         print(self.a)
#         print(self._b)
#         # print(self.__c)
#
#         self.t1()
#         self._t2()
#         # self.__t3()
#         self.__init__()
#
# p = Person()
# p.test()
#
# print(id(Animal.a))
# p.test()



#
# class B:
#     age = 10
#
#
# class A(B):
#     pass
#
#
# print(A.age)
# A.age = 9
#
# print(A.age)

# print(B.age)
# print(A.__dict__)
# print(B.__dict__)


# ------------------------继承-资源的访问顺序-2.1版本---------------------------------------

#
# class C:
#     # age = "c"
#     pass
#
# class B(C):
#     # age = "b"
#     pass
#
# class A(B):
#     # age = "a"
#     pass
#
# # A -> B -> C
# print A.age



# class E:
#     age = "e"
#
# class D:
#     # age = "d"
#     pass
#
# class C(E):
#     # age = "c"
#     pass
#
# class B(D):
#     # age = "b"
#     pass
#
# class A(B, C):
#     # age = "a"
#     pass
#
# print A.age

# A -> B -> D -> C -> E



#
# class D:
#     # age = "d"
#     pass
#
# class C(D):
#     age = "c"
#     pass
#
# class B(D):
#     # age = "b"
#     pass
#
# class A(B, C):
#     # age = "a"
#     pass
#
# print A.age
# A -> B -> D -> C


# ------------------------继承-资源的访问顺序-2.2版本---------------------------------------

import inspect

# class C(object):
#     age = "c"
#     pass
#
# class B(C):
#     # age = "b"
#     pass
#
# class A(B):
#     # age = "a"
#     pass
#
# # A -> B -> C
# print A.age
# print inspect.getmro(A)

#
# class E(object):
#     age = "e"
#
# class D(object):
#     # age = "d"
#     pass
#
# class C(E):
#     # age = "c"
#     pass
#
# class B(D):
#     # age = "b"
#     pass
#
# class A(B, C):
#     # age = "a"
#     pass
#
# print A.age
#
# print inspect.getmro(A)

# A -> B -> D -> C -> E




# class D(object):
#     age = "d"
#     pass
#
# class C(D):
#     age = "c"
#     pass
#
# class B(D):
#     # age = "b"
#     pass
#
# class A(B, C):
#     # age = "a"
#     pass
#
# print A.age
# print inspect.getmro(A)
# A -> B -> D -> C




# ------------------------继承-资源的访问顺序-2.2版本算法问题---------------------------------------



# class D(object):
#     pass
#
# class B(D):
#     pass
#
# class C(B):
#     pass
#
# class A(B, C):
#     pass
#
#
# import inspect
#
# print inspect.getmro(A)


# ------------------------继承-资源的访问顺序-2.3-2.7 C3算法---------------------------------------

# 两个公式
# 	L(object) = [object]
# 	L(子类(父类1, 父类2)) = [子类] + merge(L(父类1), L(父类2) , [父类1, 父类2])
# 注意
# 	+ 代表合并列表
# 	merge算法
# 		1. 第一个列表的第一个元素
# 			是后续列表的第一个元素
# 			或者
# 			后续列表中没有再次出现
# 			则将这个元素合并到最终的解析列表中
# 并从当前操作的所有列表中删除
# 		2. 如果不符合，则跳过此元素，查找下一个列表的第一个元素，重复1的判断规则
# 		3. 如果最终无法把所有元素归并到解析列表, 则报错

# class D(object):
#     pass

# L(D(object)) = [D] + merge(L(object), [object])
#              = [D] + merge([object], [object])
#              = [D, object] + merge([], [])
#              = [D, object]

# class B(D):
#     pass

# L(B(D)) = [B] + merge(L(D), [D])
#         = [B] + merge([D, object], [D])
#         = [B, D] + merge([object], [])
#         = [B, D, object] + merge([], [])
#         = [B, D, object]


# class C(D):
#     pass
# L(C(D)) = [C, D, object]

# class A(B, C):
#     pass
# L(A) = [A] + merge(L(B), L(C), [B, C])
#      = [A] + merge([B, D, object], [C, D, object], [B, C])
#      = [A, B] + merge([D, object], [C, D, object], [C])
#      = [A, B, C] + merge([D, object], [D, object])
#      = [A, B, C, D] + merge([object], [object])
#      = [A, B, C, D, object] + merge([], [])
#      = [A, B, C, D, object]

# import inspect
#
# print inspect.getmro(A)


# ------------------------继承-资源的访问顺序-2.3-2.7 C3算法识别问题继承-------------------------------------

#
# class D(object):
#     pass
# # L(D) = [D] + merge(L(object), [object])
# #      = [D] + merge([object], [object])
# #      = [D, object] + merge([], [])
# #      = [D, object]
#
# class B(D):
#     pass
#
# # L(B) = [B] + merge(L(D), [D])
# #      = [B] + merge([D, object], [D])
# #      = [B, D] + merge([object])
# #      = [B, D, object]
#
# class C(D):
#     pass
# # L(C) = [C] + merge(L(B) + [B])
# # L(C) = [C] + merge([B, D, object] + [B])
# # L(C) = [C, B] + merge([D, object])
# # L(C) = [C, B, D, object] + merge([])
# # L(C) = [C, B, D, object]
#
# class A(B, C):
#     pass
#

# L(A) = [A] + merge(L(B), L(C), [B, C])
# L(A) = [A] + merge([B, D, object], [C, B, D, object], [B, C])
# L(A) = [A] + merge([B, D, object], [C, B, D, object], [B, C])

# import inspect
# inspect.getmro()
#
# B.__mro__
# B.mro()


# ------------------------继承-资源的覆盖-------------------------------------



# class D(object):
#     age = "d"
#     pass
#
# class C(D):
#     age = "c"
#     def test(self):
#         print("c")
#     pass
#
# class B(D):
#     age = "b"
#     def test(self):
#         print self
#         # print("b")
#     @classmethod
#     def test2(cls):
#         print cls
#     pass
#
# class A(B, C):
#     pass
#
# A.test2()
# a = A()
# a.test()


# print(A.mro())
#
# print(A.age)
# print(A().test())


# ------------------------------继承-资源的累加-------------------------------------



#
# class B:
#     a = 1
#     def __init__(self):
#         self.b = 2
#
#     def t1(self):
#         print("t1")
#
#     @classmethod
#     def t2(cls):
#         print("t2")
#
#     @staticmethod
#     def t3():
#         print("t3")
#
#
# class A(B):
#     c = 3
#     def __init__(self):
#         self.e = "666"
#
#     def tt1(self):
#         print("t1")
#
#     @classmethod
#     def tt2(cls):
#         print("t2")
#
#     @staticmethod
#     def tt3():
#         print("t3")
#
#     pass
#
#
# a_obj = A()
#
# print(A.a)
# print(a_obj.b)
#
#
# a_obj.t1()
# A.t2()
# A.t3()
#
# print(A.c)
#
# a_obj.tt1()
# A.tt2()
# A.tt3()
#
# a_obj.d = "xxx"
# print(a_obj.d)
#
# print(a_obj.e)

# ------------------------------继承-资源的累加-2-------------------------------------

# class B:
#     a = 1
#
#     def __init__(self):
#         self.b = 2
#         self.xxx = "123"
#
#     def t1(self):
#         print("t1")
#
#     @classmethod
#     def t2(cls):
#         print("t2")
#
#     @staticmethod
#     def t3():
#         print("t3")
#
#
# class A(B):
#     c = 3
#
#     def __init__(self):
#         # self a_obj
#         # self.init
#         # b = B()
#         # b.__init__()
#         B.__init__(self)
#         # self.b = 2
#         self.e = "666"
#
#     def tt1(self):
#         print("t1")
#
#     @classmethod
#     def tt2(cls):
#         print("t2")
#
#     @staticmethod
#     def tt3():
#         print("t3")
#
#     pass
#
# a = A()
# print(a.__dict__)

# ------------------------------继承-资源的累加-2-存在问题-------------------------------------
#
# class B:
#     a = 1
#
#     def __init__(self):
#         self.b = 2
#         self.xxx = "123"
#
#     def t1(self):
#         print("t1")
#
#     @classmethod
#     def t2(cls):
#         print("t2")
#
#     @staticmethod
#     def t3():
#         print("t3")
#
#
# class A(B):
#     c = 3
#
#     def __init__(self):
#         B.__init__(self)
#         self.e = "666"
#
#     def tt1(self):
#         print("t1")
#
#     @classmethod
#     def tt2(cls):
#         print("t2")
#
#     @staticmethod
#     def tt3():
#         print("t3")
#
#     pass
#
# a = A()
# print(a.__dict__)


# class D(object):
#     def __init__(self):
#         print("d")
#
# class B(D):
#     def __init__(self):
#         D.__init__(self)
#         print("b")
#
# class C(D):
#     def __init__(self):
#         D.__init__(self)
#         print("c")
#
# class A(B, C):
#     def __init__(self):
#         B.__init__(self)
#         C.__init__(self)
#         print("a")


# B()
# C()
# A()


# ------------------------------继承-资源的累加-super使用-------------------------------------

# class B:
#     a = 1
#
#     def __init__(self):
#         self.b = 2
#         self.xxx = "123"
#
#     def t1(self):
#         print("t1")
#
#     @classmethod
#     def t2(cls):
#         print(cls)
#         print("t2")
#
#     @staticmethod
#     def t3():
#         print("t3")
#
#
# class A(B):
#     c = 3
#
#     def __init__(self):
#         # super(A, self).__init__()
#         super().__init__()
#         self.e = "666"
#
#     def tt1(self):
#         print("t1")
#
#     @classmethod
#     def tt2(cls):
#         super(A, cls).t2()
#         print("t2")
#
#     @staticmethod
#     def tt3():
#         print("t3")
#
#     pass
#
# a = A()
# # print(a.__dict__)
#
# A.tt2()

# class D(object):
#     def __init__(self):
#         print("d")
#
# class B(D):
#     def __init__(self):
#         super().__init__()
#         print("b")
#
# class C(D):
#     def __init__(self):
#         super().__init__()
#         print("c")
#
# class A(B, C):
#     def __init__(self):
#         # B.__init__(self)
#         # C.__init__(self)
#         super().__init__()
#         print("a")

# ------------------------------继承-资源的累加-super使用注意事项-------------------------------------


# class D(object):
#     def __init__(self):
#         print("d")
#
# class B(D):
#     def __init__(self):
#         super(self.__class__, self).__init__()
#         # super(A, self).__init__()
#         print("b")
#
# # class C(D):
# #     def __init__(self):
# #         super().__init__()
# #         print("c")
# # #
# class A(B):
#     def __init__(self):
#         super(A, self).__init__()
#         print("a")
#
#
# A()


# class D(object):
#     def __init__(self):
#         print("d")
#
# class B(D):
#     def __init__(self):
#         # super().__init__()
#         super(B, self).__init__()
#         print("b")
#
# class C(D):
#     def __init__(self):
#         # super().__init__()
#         super(C, self).__init__()
#         print("c")
#
# class A(B, C):
#     def __init__(self):
#         # super().__init__()
#         B.__init__(self)
#         C.__init__(self)
#         print("a")
#
#
# A()
#
# print(A.mro())











































