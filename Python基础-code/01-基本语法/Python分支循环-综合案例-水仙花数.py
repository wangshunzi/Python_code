
while True:

    # 1. 准备一个3位数的数值
    # 1.1 让用户输入数据
    num = input("请输入一个3位数值:")
    # 1.2 数据有效性的验证(保证数值, 是三位数)
    # print(len(num))
    num = int(num)
    # print(num, type(num))
    if not (100 <= num <= 999):
        print("你输入的数据无效, 直接退出程序")
        exit()

    # print("进到这一行, 就代表, 数据肯定有效")

    # 2. 根据这个三位数, 判定, 是否是水仙花数
    # 百位的3次方 + 十位的3次方 + 个位的3次方
    # 	= 数值本身

    # 2.1 分解数值 -> 百位, 十位, 个位
    # 123 = 1, 2, 3
    baiwei = num // 100
    shiwei = num % 100 // 10
    gewei = num % 10



    # 2.2 直接套入公式, 判定,是否是水仙花数
    result = (baiwei ** 3 + shiwei ** 3 + gewei ** 3 == num)



    # 3. 打印结果
    # 直接打印, 判定好的结果
    if result:
        print("%d, 是水仙花数"%num)
    else:
        print("%d, 不是水仙花数" % num)