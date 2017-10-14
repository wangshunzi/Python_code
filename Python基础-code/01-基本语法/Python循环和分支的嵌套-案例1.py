
# 打印1-100之间, 所有3的倍数



# 1. 先造一个集合
nums = range(1, 101)
print(nums)
# 2. 遍历集合
for num in nums:
    if num % 3 == 0:
        print(num)
# 3. 就是在这个遍历的过程当中, 来判定这个集合里面的元素, 是否, 可以被3 整除

