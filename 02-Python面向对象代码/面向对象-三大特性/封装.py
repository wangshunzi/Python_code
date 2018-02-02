# _*_ encoding:utf-8 _*_
# import win32com.client
#
#
class Caculator(object):
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
        self.__say("sz牌计算机计算的结果是:%d" % self.__result)
        print("计算的结果是:%d" % self.__result)
        return self

    def clear(self):
        self.__result = 0
        return self

    @property
    def result(self):
        return self.__result
