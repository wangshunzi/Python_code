

# abs(num)
# 	返回数字的绝对值


num = -10
print(abs(num))


# 最大值,
print(max(
    1, 12, 3, 5
))


# 最小值
print(min(
    1, 12, 3, 5
))

print(min([1, 3, 5, 2]))


# round(num[, n])
# 	四舍五入
# 	, n
# 		表示四舍五入的位数
# 		可以省略

p = 3.147
print(round(p, 2))

# # pow(x, y)
# 	返回 x 的 y次幂
# 		x ** y

print(pow(2, 14))
print(2 ** 14)




# math模块函数

# 导入模块math
import math

# math.函数名称(参数)

p1 = 3.9
print(round(p1))
print(math.ceil(p1))

print(math.floor(p1))



print(math.sqrt(17))



print(math.log(10000, 100))

import random
print(random.random(1, 3))
