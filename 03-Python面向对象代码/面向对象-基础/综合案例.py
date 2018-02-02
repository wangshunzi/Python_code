# _*_ encoding:utf-8 _*_

# 计算器, 实现一些基本的操作, 加减乘除运算, 以及打印结果操作

# ------------------------------------代码1--------------------------------------
# def jia(n1, n2):
#     return n1 + n2
#
# def jian(n1, n2):
#     return n1 - n2
#
# def cheng(n1, n2):
#     return n1 * n2
#
# # res = jia(2, 4)
# # res2 = cheng(5, 7)
# # print(res)
# # print(res2)
# # (2 + 6 - 4) * 5
#
# r1 = jia(2, 6)
# r2 = jian(r1, 4)
# r3 = cheng(r2, 5)
# print(r3)

# ------------------------------------代码2--------------------------------------
# result = 0
#
# def first_value(v):
#     global result
#     result = v
#
# def jia(n):
#     global result
#     result += n
#
# def jian(n):
#     global result
#     result -= n
#
# def cheng(n):
#     global result
#     result *= n
#
#
# first_value(2)
# jia(6)
# result = 123
# jian(4)
# cheng(5)
# print(result)

# ------------------------------------代码3--------------------------------------


# class Caculator:
#     __result = 0
#
#     @classmethod
#     def first_value(cls, v):
#         cls.__result = v
#
#     @classmethod
#     def jia(cls, n):
#         cls.__result += n
#
#     @classmethod
#     def jian(cls, n):
#         cls.__result -= n
#
#     @classmethod
#     def cheng(cls, n):
#         cls.__result *= n
#
#     @classmethod
#     def show(cls):
#         print("计算的结果是:%d" % cls.__result)
#
# Caculator.first_value(2)
# Caculator.jia(6)
# Caculator.jian(4)
# Caculator.cheng(5)
# Caculator.show()

# ------------------------------------代码4--------------------------------------
#
# class Caculator:
#
#     def __init__(self, num):
#         self.__result = num
#
#     def jia(self, n):
#         self.__result += n
#
#     def jian(self, n):
#         self.__result -= n
#
#     def cheng(self, n):
#         self.__result *= n
#
#     def show(self):
#         print("计算的结果是:%d" % self.__result)
#
#
# c1 = Caculator(2)
# c1.jia(6)
# c1.jian(4)
# c1.cheng(5)
# c1.show()

# ------------------------------------代码5--------------------------------------


# class Caculator:
#     def check_num(self, num):
#         if not isinstance(num, int):
#             raise TypeError("当前这个数据的类型有问题, 应该是一个整型数据")
#
#     def __init__(self, num):
#         self.check_num(num)
#         self.__result = num
#
#     def jia(self, n):
#         self.check_num(n)
#         self.__result += n
#
#     def jian(self, n):
#         self.check_num(n)
#         self.__result -= n
#
#     def cheng(self, n):
#         self.check_num(n)
#         self.__result *= n
#
#     def show(self):
#         print("计算的结果是:%d" % self.__result)
#
#
# c1 = Caculator(2)
# c1.jia(6)
# c1.jian("a")
# c1.cheng(5)
# c1.show()

# ------------------------------------代码6--------------------------------------
#
# class Caculator:
#     def check_num_zsq(func):
#         def inner(self, n):
#             if not isinstance(n, int):
#                 raise TypeError("当前这个数据的类型有问题, 应该是一个整型数据")
#             return func(self, n)
#         return inner
#
#     @check_num_zsq
#     def __init__(self, num):
#         self.__result = num
#
#     @check_num_zsq
#     def jia(self, n):
#         self.__result += n
#
#     @check_num_zsq
#     def jian(self, n):
#         self.__result -= n
#
#     @check_num_zsq
#     def cheng(self, n):
#         self.__result *= n
#
#     def show(self):
#         print("计算的结果是:%d" % self.__result)
#
#
# c1 = Caculator(2)
# c1.jia(6)
# c1.jian(4)
# c1.cheng(5)
# c1.show()

# ------------------------------------代码7--------------------------------------


# class Caculator:
#     def __check_num_zsq(func):
#         def inner(self, n):
#             if not isinstance(n, int):
#                 raise TypeError("当前这个数据的类型有问题, 应该是一个整型数据")
#             return func(self, n)
#         return inner
#
#     @__check_num_zsq
#     def __init__(self, num):
#         self.__result = num
#
#     @__check_num_zsq
#     def jia(self, n):
#         self.__result += n
#
#     @__check_num_zsq
#     def jian(self, n):
#         self.__result -= n
#
#     @__check_num_zsq
#     def cheng(self, n):
#         self.__result *= n
#
#     def show(self):
#         print("计算的结果是:%d" % self.__result)
#
#
# c1 = Caculator(2)
# c1.jia(6)
# c1.jian(4)
# c1.cheng(5)
# c1.show()


# ------------------------------------代码8--------------------------------------
import win32com.client

# # 1. 创建一个播报器对象
# speaker = win32com.client.Dispatch("SAPI.SpVoice")
#
# # 2. 通过这个播报器对象, 直接, 播放相对应的语音字符串就可以
# speaker.Speak("我的名字是sz")

# class Caculator:
#     def __check_num_zsq(func):
#         def inner(self, n):
#             if not isinstance(n, int):
#                 raise TypeError("当前这个数据的类型有问题, 应该是一个整型数据")
#             return func(self, n)
#
#         return inner
#
#     # def __say(self, word):
#     #     # 1. 创建一个播报器对象
#     #     speaker = win32com.client.Dispatch("SAPI.SpVoice")
#     #
#     #     # 2. 通过这个播报器对象, 直接, 播放相对应的语音字符串就可以
#     #     speaker.Speak(word)
#
#     def create_say_zsq(word=""):
#         def __say_zsq(func):
#             def inner(self, n):
#                 # 1. 创建一个播报器对象
#                 speaker = win32com.client.Dispatch("SAPI.SpVoice")
#                 # 2. 通过这个播报器对象, 直接, 播放相对应的语音字符串就可以
#                 speaker.Speak(word + str(n))
#                 return func(self, n)
#
#             return inner
#
#         return __say_zsq
#
#     @__check_num_zsq
#     @create_say_zsq()
#     def __init__(self, num):
#         self.__result = num
#
#     @__check_num_zsq
#     @create_say_zsq("加")
#     def jia(self, n):
#         self.__result += n
#
#     @__check_num_zsq
#     @create_say_zsq("减去")
#     def jian(self, n):
#         self.__result -= n
#
#     @__check_num_zsq
#     @create_say_zsq("乘以")
#     def cheng(self, n):
#         self.__result *= n
#
#     def show(self):
#         # self.__say("计算的结果是:%d" % self.__result)
#         print("计算的结果是:%d" % self.__result)
#
# c1 = Caculator(10)
# c1.jia(6)
# c1.jian(4)
# c1.cheng(5)
# c1.show()

# ------------------------------------代码9--------------------------------------
# import win32com.client
#
#
# class Caculator:
#     def __check_num_zsq(func):
#         def inner(self, n):
#             if not isinstance(n, int):
#                 raise TypeError("当前这个数据的类型有问题, 应该是一个整型数据")
#             return func(self, n)
#
#         return inner
#
#     def __say(self, word):
#         # 1. 创建一个播报器对象
#         speaker = win32com.client.Dispatch("SAPI.SpVoice")
#
#         # 2. 通过这个播报器对象, 直接, 播放相对应的语音字符串就可以
#         speaker.Speak(word)
#
#     def __create_say_zsq(word=""):
#         def __say_zsq(func):
#             def inner(self, n):
#                 self.__say(word + str(n))
#                 return func(self, n)
#
#             return inner
#         return __say_zsq
#
#     @__check_num_zsq
#     @__create_say_zsq()
#     def __init__(self, num):
#         self.__result = num
#
#     @__check_num_zsq
#     @__create_say_zsq("加")
#     def jia(self, n):
#         self.__result += n
#
#     @__check_num_zsq
#     @__create_say_zsq("减去")
#     def jian(self, n):
#         self.__result -= n
#
#     @__check_num_zsq
#     @__create_say_zsq("乘以")
#     def cheng(self, n):
#         self.__result *= n
#
#     def show(self):
#         self.__say("计算的结果是:%d" % self.__result)
#         print("计算的结果是:%d" % self.__result)
#
# c1 = Caculator(10)
# c1.jia(6)
# c1.jian(4)
# c1.cheng(5)
# c1.show()


# ------------------------------------代码10--------------------------------------
# import win32com.client
#
#
# class Caculator:
#     def __check_num_zsq(func):
#         def inner(self, n):
#             if not isinstance(n, int):
#                 raise TypeError("当前这个数据的类型有问题, 应该是一个整型数据")
#             return func(self, n)
#
#         return inner
#
#     def __say(self, word):
#         # 1. 创建一个播报器对象
#         speaker = win32com.client.Dispatch("SAPI.SpVoice")
#
#         # 2. 通过这个播报器对象, 直接, 播放相对应的语音字符串就可以
#         speaker.Speak(word)
#
#     def __create_say_zsq(word=""):
#         def __say_zsq(func):
#             def inner(self, n):
#                 self.__say(word + str(n))
#                 return func(self, n)
#
#             return inner
#         return __say_zsq
#
#     @__check_num_zsq
#     @__create_say_zsq()
#     def __init__(self, num):
#         self.__result = num
#
#     @__check_num_zsq
#     @__create_say_zsq("加")
#     def jia(self, n):
#         self.__result += n
#
#     @__check_num_zsq
#     @__create_say_zsq("减去")
#     def jian(self, n):
#         self.__result -= n
#
#     @__check_num_zsq
#     @__create_say_zsq("乘以")
#     def cheng(self, n):
#         self.__result *= n
#
#     def show(self):
#         self.__say("计算的结果是:%d" % self.__result)
#         print("计算的结果是:%d" % self.__result)
#
#     @property
#     def result(self):
#         return self.__result
#
# c1 = Caculator(10)
# c1.jia(6)
# c1.jian(4)
# c1.cheng(5)
# c1.show()
#
# print(c1.result)
# c1.result = 10

# ------------------------------------代码11--------------------------------------
import win32com.client


class Caculator:
    def __check_num_zsq(func):
        def inner(self, n):
            if not isinstance(n, int):
                raise TypeError("当前这个数据的类型有问题, 应该是一个整型数据")
            return func(self, n)

        return inner

    def __say(self, word):
        # 1. 创建一个播报器对象
        speaker = win32com.client.Dispatch("SAPI.SpVoice")

        # 2. 通过这个播报器对象, 直接, 播放相对应的语音字符串就可以
        speaker.Speak(word)

    def __create_say_zsq(word=""):
        def __say_zsq(func):
            def inner(self, n):
                self.__say(word + str(n))
                return func(self, n)

            return inner
        return __say_zsq

    @__check_num_zsq
    @__create_say_zsq()
    def __init__(self, num):
        self.__result = num

    @__check_num_zsq
    @__create_say_zsq("加")
    def jia(self, n):
        self.__result += n
        return self

    @__check_num_zsq
    @__create_say_zsq("减去")
    def jian(self, n):
        self.__result -= n
        return self

    @__check_num_zsq
    @__create_say_zsq("乘以")
    def cheng(self, n):
        self.__result *= n
        return self

    def show(self):
        self.__say("计算的结果是:%d" % self.__result)
        print("计算的结果是:%d" % self.__result)
        return self

    def clear(self):
        self.__result = 0
        return self

    @property
    def result(self):
        return self.__result

c1 = Caculator(10)
c1.jia(6).jian(4).cheng(5).show().clear().jia(555).jian(500).show()

print(c1.result)


