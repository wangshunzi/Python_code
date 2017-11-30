
import random

# random()
# 	[0, 1)
# 		范围之内的随机小数


print(random.random())


# choice(seq)
# 	从一个序列中, 随机挑选一个数值
# 	random.choice((1, 3, 6, 8))

seq = [1, 3, 5, 6, 8, 9]
print(random.choice(seq))


# uniform(x, y)
# 	[x, y]
# 		范围之内的随机小数

print(random.uniform(1, 3))

#
# randomint(x, y)
# 	[x, y]
# 		范围之内的随机整数

print(random.randint(1, 3))

#
# randrange(start, stop=None, step=1)
# 	给定区间内的一随机整数
# 	[start, stop)

print(random.randrange(1, 14, 2))