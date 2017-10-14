# _*_ coding:utf-8 _*_

# # 算术运算符
# # 	+
# # 		加法运算符
#
# print(1 + 2)
# # print("1" + "2")
# # print([1, 2] + [3, 4])
#
#
#
# # 	-
# # 		减法运算符
# print(4 - 12)
#
#
# # 	*
# # 		乘法运算符
#
# print(2 * 3)
#
# # 	**
# # 		幂运算符
# print(3 ** 5)
#
#
#
# # 	/
# # 		除法运算符
#
# print(5 / 2)
# # print(5 / 0)
#
#
# # 	//
# # 		整除运算符
# print(5.2 // 2)  # 5.2 / 2 = 2.6
#
#
#
# # 	%
# # 		求模运算符, 求余运算符
# #  5 / 2 = 2 (1)
# # print(5 % 2)
# # 10 / 4 = 2 (2)
# print(10 % 4)
#
#
#
# # 	=
# # 		赋值运算符
# # 			a = 10
# # 			b = a + c
# # 			a, b, c = 10, 20, 30
# #
#
#
#
#
# # 	注意
# # 		除以0
# # 		优先级问题
# # 			()使用
#
# result = (1 + 2) * 3 / 4
# print(result)
#
#
#
# # 	整除和求余的应用场景
# # 		行列
#
#
# num = 6
# row = num // 4
# col = num % 4
#


# num = 10
# result = num + 5
# num = result
# print(num)

# num = 10
# num = num + 5
# print(num)


# num = 10
# num += 5
# # num = num + 5
# print(num)


# num = 10
# # num *= 20
# num = num * 20
# print(num)


# num = 10
# num **= 2
# # num = num * 20
# print(num)



# 是否大于 是 否 Bool
# result = 10 <= 10
# print(result)


# print (10 == 10)


# num = 10
# print id(num)


# a = 10
# b = 10
# print id(a), id(b)
# print a is b


# a = [1]
# b = [1]
# print a == b
# print id(a), id(b)
# print a is b
#
#



b = False
# not 非, 取反, 真 -> 假; 假 -> 真
# 一元运算符
print(not b)

# and 与, 并且, and的两边, 必须都是真, 最终才会是真
# 一假全假
# 身份证  并且 成年 => 上网
print(True and True)


# or 或, 或者, or的两边, 只要有一个条件是真的, 那么最终都是真的
# 一真全真
# # 门开了 或者 窗户开了 => 进入到房间
# print(True or False)
#
# print(1 or False)


print(0 and True)
print(1 and 3)
print(0 or False or 6)


# print(bool(""))

