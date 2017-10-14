#
# bbbbb = 10
#
# def test():
#     a = 1
#     print(b)
#     def test2():
#         print(a)
#         c = 111
#         print(b)
#
#
# # print(b)
# test()
#
# import os
#
# os.remove()
#
# xxx.remove()
#
# __name__


# if True:
#     a = 10
#
# print(a)

# -----------------------局部变量 全局变量----------------------------
# a = 999
#
# def test():
#     # a = 1
#     # a = 2
#     print(a)
#     def test2():
#         # nonlocal a
#         # a = 10
#         print(a)
#     test2()
#     print(a)
#
# test()

# print(a)
# a = 999
# b = 10
#
# def test():
#     # 这里如果, 直接使用赋值表达式, 赋值给一个变量, 其实是代表,定义一个新的变量
#     global a
#     a = 6
#     print(a)
#     # def tes2():
#     #     nonlocal a
#     #     a = 77
#     b = 10
#     c = 0
#     print(locals())
#     print(globals())
# # print(a)
# test()
# # print(a)
#
#
# print(b)



g_a = 1
g_b = 10
def test():
    print(g_a)
    print(g_b)

test()




















