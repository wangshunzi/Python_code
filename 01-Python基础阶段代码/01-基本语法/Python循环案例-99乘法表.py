

# 给定一个数值, 打印出, 从1, - 这个数值之间所有的数字


# num = 3
#
# # 1. 造一个集合
# nums = range(1, num + 1)
# # 2. 遍历这个集合
# for n in nums:
#     # 3. 在遍历的过程当中, 打印每一个元素
#     # print(n)
#     # x * x = x
#     print("%d * %d = %d"%(n, num, n * num), end="\t")

    # 1 * 1 = 1
    # 1 * 2 = 2	2 * 2 = 4
    # 1 * 3 = 3	2 * 3 = 6	3 * 3 = 9




# 获取, 1-9这样的一个集合, 然后, 再遍历这个集合, 分别取出里面的1-9这些数字

for num in range(1, 10):

    # 1. 造一个集合
    nums = range(1, num + 1)
    # 2. 遍历这个集合
    for n in nums:
        # 3. 在遍历的过程当中, 打印每一个元素
        # print(n)
        # x * x = x
        print("%d * %d = %d" % (n, num, n * num), end="\t")
    print("")