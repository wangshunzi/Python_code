# _*_ coding:utf-8 _*_
# 1 / 0
# ZeroDivisionError
# def divide(x, y):
#     if y != 0:
#         return x / y
#     print("除数不能为0, 请仔细检查")
#     return 0
#
#
# print(divide(1, 0))
#
# if name != None:
#     print(name)
# NameError


# print(name)
# print("123")



# try:
#     print(name)
# except NameError:
#     print("名称有问题, 请仔细检查")


# try:
#     # 1 / 0
#     print(name)
# except ZeroDivisionError as ze:
#     print("xxx", ze)
# except NameError as ne:
#     print("名称错误", ne)
# else:
#     print("123")
# finally:
#     print("最后执行的内容, 到时候, 不管是否会出现异常, 都会执行的语句")


# try:
#     1 / 0
#     # print(name)
# except Exception as e:
#     print("xxx", e)
# else:
#     print("123")
# finally:
#     print("最后执行的内容, 到时候, 不管是否会出现异常, 都会执行的语句")

# try:
#     f = open("xx.jpg", "r")
#     f.readlines()
# except Exception as e:
#     print(e)
# finally:
#     print("xxxx")
#     f.close()

# with open("xx.jpg", "r") as f:
#     f.readlines()


# class Test:
#     def __enter__(self):
#         print("enter")
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print(self, exc_type, exc_val, exc_tb)
#         import traceback
#         print(traceback.extract_tb(exc_tb))
#         print("exit")
#         return True
#
# with Test() as x:
#     # print("body", x)
#     1 / 0


import contextlib


class Test:
    def t(self):
        print("tttttt")

    def close(self):
        print("资源释放")

    # def __enter__(self):
    #     return self
    #
    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     self.close()
# import contextlib
# with contextlib.closing(Test()) as t_obj:
#     t_obj.t()


# with open("xx.jpg", "rb") as from_file:
#     with open("xx2.jpg", "wb") as to_file:
#         from_contents = from_file.read()
#         to_file.write(from_contents)
# with open("xx.jpg", "rb") as from_file, open("xx2.jpg", "wb") as to_file:
#     from_contents = from_file.read()
#     to_file.write(from_contents)
# import contextlib
# with contextlib.nested(open("xx.jpg", "rb"), open("xx2.jpg", "wb")) as (from_file, to_file):
#     from_contents = from_file.read()
#     to_file.write(from_contents)

class LessZero(Exception):
    def __init__(self, msg, error_code):
        self.msg = msg
        self.ec = error_code

    def __str__(self):
        return self.msg + str(self.ec)
    pass


def set_age(age):
    if age <=0 or age > 200:
        # print("值错误")
        raise LessZero("小于零, 错误", 404)
    else:
        print("给张三的年龄设置为", age)


try:
    set_age(-18)
except LessZero as e:
    print("x", e)



















