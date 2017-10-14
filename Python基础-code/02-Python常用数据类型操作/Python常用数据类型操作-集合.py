# str1 = "abca"
# l = [1, 2, 1, 3]
# t = (1, 2, 3, 3)
# d = {"name": "sz", "age": 18, "add": 18}
#
# s = {1, 2, 3, 1}

# 集合的定义
# 可变集合
#
# s = {1, 2, 3}
# print(s, type(s))
#
#
#
# # s2 = set("abc")
# # s2 = set([1, 2, 3])
# s2 = set({"name": "sz", "Age": 18})
# # s2 = set((1, 2, 3))
# print(s2, type(s2))


# s = set(x for x in range(0, 10))
# s = {x for x in range(0, 10)}
# print(s, type(s))




# 可变集合的定义

# fs = frozenset("abc")
# fs = frozenset([1, 2, 3])
# fs = frozenset((1, 2, 3))
# fs = frozenset({"name": "sz", "age": 18})
# print(fs, type(fs))


# s = frozenset(x ** 2 for x in range(1, 10) if x % 2 == 0)
# print(s, type(s))


# s = {}
# s = set()
# s = frozenset()
# s = {1, 2, [1, 2]}
# s = {1, 2, {"name": "sz"}}
# s = {1, 2, 1}
# print(s, type(s))


# l = [1, 2, 3, 3, 3]
# s = set(l)
# print(s)
# result = list(s)
# print(result, type(result))




# --------------------------集合的操作----------------------------------




# s = {1, 2, 3}
# # s.add(4)
# s.add([1, 2])
# print(s, type(s))


# 删
# 	s.remove(element)
# 		指定删除set对象中的一个元素
# 		如果集合中没有这个元素，则返回一个错误

# s = {1, 2, 3}
# result = s.remove(3)
# result = s.remove(13)
# print(result, s)


# 	s.discard(element)
# 		指定删除集合中的一个元素
# 		若没有这个元素，则do nothing
# result = s.discard(13)
# print(result, s)



# 	s.pop(element)
# 		随机删除并返回一个集合中的元素
# 		若集合为空，则返回一个错误
# result = s.pop()
# print(result, s)
#
# result = s.pop()
# print(result, s)
#
# result = s.pop()
# print(result, s)
#
# result = s.pop()
# print(result, s)

# 	s.clear()
# 		清空一个集合中的所有元素
# result = s.clear()
# print(result, s)



# s = {1, 2, 3}
# s = frozenset([1, 2, 3])
# print(s, type(s))

# for v in s:
#     print(v)


# 1. 生成一个迭代器
# its = iter(s)

# 2. 使用这个迭代器去访问(next(), for in)
# print(next(its))
# print(next(its))
# print(next(its))
# print(next(its))

# print("-------")
#
# for v in its:
#     print(v)


# -----------------------------集合之间的操作----------------------------------


# 交集
# 	intersection(Iterable)
# 		字符串
# 			只判定字符串中的非数字
# 		列表
# 		元组
# 		字典
# 			值判定key
# 		集合
# 		...
# 	逻辑与 '&'
# 	intersection_update(…)
# 		交集计算完毕后, 会再次赋值给原对象
# 			会更改原对象
# 			所以, 只适用于可变集合

# s1 = {"1", "2", "3", "4", "5"}
# s1 = frozenset([1, 2, 3, 4, 5])
# s2 = {4, 5, 6}
# result = s2.intersection_update(s1)
# # result = s2 & s1
# print(result, type(result))
# print(s1, s2)


# print(s1.intersection("123"))
# print(s1.intersection({"1": "abc", "2": "12", "6": 18}))
# print(s1.intersection(["1", "2", ["1", "2"]]))




# 并集
# 	union()
# 		返回并集
# 	逻辑或 '|'
# 		返回并集
# 	update()
# 		更新并集

# s1 = {1, 2, 3}
# s1 = frozenset([1, 2, 3])
# s2 = {3, 4, 5}

# result = s1.union(s2)
# result = s1 | s2
# result = s1.update(s2)
# print(result, s1)





# 差集
# 	difference()
# 	算术运算符减 ‘-‘
# 	difference_update()

# s1 = {1, 2, 3}
# s2 = {3, 4, 5}
#
# # result = s1.difference(s2)
# result = s1.difference_update(s2)
# # result = s1 - s2
# print(result, s1)



# 判定
# 	isdisjoint()两个集合不相交
# 	issuperset()一个集合包含另一个集合
# 	issubset()一个集合包含于另一个集合

s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6}
# print(s1.isdisjoint(s2))
# print(s1.issuperset(s2))
print(s2.issubset(s1))








