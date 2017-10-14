



# l = [i for i in range(1, 10000000) if i % 2 == 0]
# l = (i for i in range(1, 10000000) if i % 2 == 0)
#
# print(next(l))
# print(next(l))
# print(l.__next__())
#
# for i in l:
#     print(i)




# 生成器的创建方式2
# yied, 可以去阻断当前的函数执行, 然后, 当使用next()函数, 或者, __next__(), 都会让函数继续执行, 然后, 当执行到下一个 yield语句的时候, 又会被暂停
# def test():
#     print("xxx")
#     yield 1
#     print("a")
#
#     yield 2
#     print("b")
#
#     yield 3
#     print("c")
#
#     yield 4
#     print("d")
#
#     yield 5
#     print("e")

#
# def test():
#     for i in range(1, 9):
#         yield i
#
# g = test()
# print(g)
#
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))


# def test():
#     # print("xxx")
#     res1 = yield 1 # "ooo"
#     print(res1)
#
#     res2 = yield 2
#     print(res2)
#
# g = test()
#
# # print(g.__next__())
# # print(g.__next__())
# # print(g.send("ooo"))
# print(g.send(None))
# print(g.send(666))


#
# def test():
#     yield 1
#     print("a")
#
#     yield 2
#     print("b")
#
#     yield 3
#     print("c")
#
#     return 10
#
#
#
# g = test()
#
# print(g.__next__())
# print(g.__next__())
#
# g.close()
#
# print(g.__next__())
# # print(g.__next__())



def test():
    yield 1
    print("a")

    # return 10

    yield 2
    print("b")

    yield 3
    print("c")




# g = test()
#
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

g = test()
for i in g:
    print(i)

print("-"*30)
g = test()
for i in g:
    print(i)










