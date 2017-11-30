
import random

# 1. 准备数据
num = random.randint(1, 500)

count = 0

while True:
    # 2. 数据处理
    count += 1
    # 2.1 让用户输入一个结果
    result = input("请输入结果:")
    result = int(result)


    # 2.2 拿用户所输入的数值, 和给定的一个数值进行比对
    # 2.2.1 如果是相等 -> 给出一个正确的提示, 然后, 结束程序
    if result == num:
        print("恭喜你, 猜对了, 答案就是%d, 你总共猜了%d次"%(result, count))
        # exit()
        break
    # else:
    # 2.2.2 如果值, 不相等,
    # 2.2.2.1 判定数值关系, 给出不同的提示
    # 2.2.2.1.1 如果大于 -> 你猜的数字, 太大了, 应该小一点
    if result > num:
        print("你猜的数字, 太大了, 应该小一点")
    # 2.2.2.1.2 如果小于 -> 你猜的数字, 太大小了, 应该大一点
    else:
        print("你猜的数字, 太小了, 应该大一点")


    # 2.2.2.2 让用户, 继续猜