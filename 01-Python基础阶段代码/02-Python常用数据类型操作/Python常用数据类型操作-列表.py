
#_*_ encoding:utf-8 _*_

# ------------------------------列表的定义方式1-----------------------------------
# names = ["zhangsan", "lisi", "wanger"]
# names = [1, True, 3, "sz"]
# names = []

# items = ["a", "b", "c"]
# # names = [1, 2, 3, "sz", True, items]
# names = [1, 2, 3, 'sz', True, ['a', 'b', 'c']]
#
# print(names, type(names))

# ------------------------------列表的定义方式2-----------------------------------


# [1, 2, 3, 4, 5]


# 0 - 99 [1, 2, 3, ... 99]
# nums = range(99)
# nums = range(1, 10000)
# print(nums)


nums = [1, 2, 3, 4, 5]

# 原始的方式
# resultList = []
# for num in nums:
#     # print(num)
#     if num % 2 == 0:
#         continue
#     resultNum = num ** 2
#     print(resultNum)
#     resultList.append(resultNum)
#
# print(resultList)

# 列表推导式
# resultList = [num ** 2 for num in nums if num % 2 != 0]
resultList = [num ** 2 for num in nums for num2 in nums]
print(resultList)














