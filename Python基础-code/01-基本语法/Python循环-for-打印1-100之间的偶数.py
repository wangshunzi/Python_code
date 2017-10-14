
# 打印1-100之间的偶数
# 1 - 100这样的集合
# 函数 -> range
# 怎样去判定一个数值, 是偶数 2
for num in range(1, 101):
    if num % 2 == 0:
        print(num, "是偶数")
