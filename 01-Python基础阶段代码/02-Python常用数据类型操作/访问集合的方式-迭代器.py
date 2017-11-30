

nums = [1, 2]

# for num in nums:
#     print(num)

import collections
result = isinstance(nums, collections.Iterable)
print(result)


# result2 = isinstance(nums, collections.Iterator)
# print(result2)
#
# next(nums)


# i = iter(nums)
# print(i)
# result = isinstance(i, collections.Iterable)
# print(result)

# [0, 1, 1, 2, 3, 5, 8]
#
#
#
# "abc" 123
# [1, 2, 3] 456
# (1, 2) 789
#
#
# bianlinag = 集合
#
# # 写一个统一的遍历代码



l = [1, 2, 3, 4, 5]

# 1. 创建一个迭代器对象
it = iter(l)

# next()
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

for v in it:
    print(v)

print("-------")

for v in it:
    print(v)