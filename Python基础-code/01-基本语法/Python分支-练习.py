# 0 -- 100
# 根据分数区间, 打印出对应的级别
# 大于等于90  并且 小于等于100
# 	 优秀
# 大于等于80  并且 小于90
# 	良好
# 大于等于60  并且 小于80
# 	及格
# 大于等于0  并且 小于60
# 	不及格


score = 85

# if score >= 90 and score <= 100:
#     print("优秀")
#
# if score >= 80 and score < 90:
#     print("良好")
#
# if score >= 60 and score < 80:
#     print("及格")
#
# if score >=0 and score < 60:
#     print("不及格")

# 可阅读性比较差
# if 90 <= score <= 100:
#     print("优秀")
# else:
#     if 80 <= score < 90:
#         print("良好")
#     else:
#         if 60 <= score < 80:
#             print("及格")
#         else:
#             if 0 <= score < 60:
#                 print("不及格")

if 90 <= score <= 100:
    print("优秀")
elif 80 <= score < 90:
    print("良好")
elif 60 <= score < 80:
    print("及格")
elif 0 <= score < 60:
    print("不及格")


# if 10 > 2:
#     print("1")
#     print("1")
#     print("1")
#     print("1")
#
# print("2")


if 2 > 1:
    if 2 > 3:
        print("xxx")
else:
        print("ooo")
