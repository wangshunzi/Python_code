# _*_encoding:utf-8_*_
# 表述一个人的一些信息, 姓名 年龄 身高

# str1 = "sz,18,180"
# infos = str1.split(",")
# print(infos)
#
#
# l = ['sz', '18', '180']
# l[0]
# l[1]
# l[2]
#
#
# t = ('sz', '18', '180')
# t[0]
# t[1]
# t[2]



# person = {"name": "sz", "age": 18}
# print(person, type(person))
# print(person["name"])
# print(person["age"])

# d = dict.fromkeys("abc", 666)
# d = {1: 2, 2: 3}.fromkeys([1, 2, 3], 666)
# print(d)



# d = {1: "a", 2: "b", 1: "c"}
# print(d)

# d = {[1, 2, 3]: "123"}
# print(d)


# num = [1, 2, 3]
# print(num, id(num))
#
# num.append(4)
# print(num, id(num))


# ------------------------------字典的常用操作----------------------------------

# 增
# 	dic[key] = value
# 		当key在原字典中不存在时, 即为新增操作

# d = {"name": "sz", "age": 18}
# print(d, type(d), id(d))
#
# d["height"] = 180
# print(d, type(d), id(d))


# 删
# del dic[key]
# d = {"name": "sz", "age": 18}
# del d["age1"]
# print(d)


# dic.pop(key[, default])
# 删除指定的键值对, 并返回对应的值
# 如果key, 不存在, 那么直接返回给定的default值;
# 不作删除动作
# 如果没有给定默认值, 则报错

# v = d.pop("age")
# print(v, d)

# v = d.pop("age1", 666)
# print(v, d)





# dic.popitem()
# 删除按升序排序后的第一个键值对, 并以元组的形式返回该键值对
# 如果字典为空, 则报错

# d = {"name": "sz", "zge": 18, "a": 123}
# d = {}
# result = d.popitem()
# print(result, d)





# dic.clear()
# 删除字典内所有键值对
# 返回None
# 注意, 字典对象本身还存在, 只不过内容被清空
# 注意和del的区别

# d = {"name": "sz", "zge": 18, "a": 123}
# print(d.clear())
# print(d)

# del d
# print(d)





# 改
# 	只能改值, 不能改key
# 	修改单个键值对
# 		dic[key] = value
# 			直接设置, 如果key不存在, 则新增, 存在则修改
# d = {"name": "sz", "age": 18}
# print(d)
# d["age1"] = 20
# print(d)



# 	批量修改键值对
# 		oldDic.update(newDic)
# 			根据新的字典, 批量更新旧字典中的键值对
# 			如果旧字典没有对应的key, 则新增键值对
# d = {"name": "sz", "age": 18}
#
# d.update({"age": 666, "address": "上海"})
# print(d)


# ---------------------查询操作----------------------------


# 获取单个值
# 方式1
# dic[key]
# 如果key, 不存在, 会报错
# d = {"name": "sz", "age": 18, 0: "666"}
# # print(d["age"])
# print(d[0])




# 方式2
# dic.get(key[, default])
# 如果不存在对应的key, 则取给定的默认值default
# 如果没有默认值, 则为None
# 但不会报错
# 但是, 原字典不会新增这个键值对
# d = {"name": "sz", "age": 18, 0: "666"}
# v = d.get("age1", 666)
# print(v, d)



# 方式3
# dic.setdefault(key[, default])
# 获取指定key对应的值
# 如果key不存在, 则设置给定默认值, 并返回该值
# 如果默认值没给定
# 则使用None代替
# d = {"name": "sz", "age": 18, 0: "666"}
# v = d.setdefault("age1", 666)
# print(v, d)







# 获取所有的值
# 	dic.values()
# d = {"name": "sz", "age": 18, 0: "666"}
# vs = d.values()
#
#
# # 获取所有的键
# # 	dic.keys()
# ks = d.keys()
#
#
#
# # 获取字典的键值对
# # 	dic.items()
# its = d.items()
#
#
# print(vs, ks, its)
#
#
# d["address"] = 999
# print(d)
#
# print(vs, ks, its)
#
# print(list(vs))
# print(tuple(vs))



# 先遍历所有的key< 然后, 根据指定的key, 获取到对应的值
# d = {"name": "sz", "age": 18, "address": "上海"}

# 1. 先获取所有的key
# keys = d.keys()
#
# # 2. 遍历所有de key
# for key in keys:
#     print(key)
#     print(d[key])
#
#
#
#
# # 直接遍历所有的键值对
#
# # 1. 获取, 所有的键值对
# kvs = d.items()
# print(kvs)
# # [('name', 'sz'), ('age', 18), ('address', '上海')]
#
# d["xxx"] = "000"
#
# # 2. 直接遍历
#
# for k, v in kvs:
#     print(k, v)

d = {"name": "sz", "age": 18, "address": "上海"}

# 计算
# 	len(info)
# 		键值对的个数
print(len(d))



# 判定
# 	x in dic
# 		判定dic中的key, 是否存在x
print(18 in d)

# 	x not in dic
# 		判定dic中的key, 是否不存在x



# 	dic.has_key(key)
# 		已过期, 建议使用in来代替
print(d.has_key("name"))



















