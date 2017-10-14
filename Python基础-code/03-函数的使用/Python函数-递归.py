



# 9
# 1 * 2 * 3 * ... 9



# 9! = 9 * 8!
#         8 * 7!
#             7 * 6!
#                ....
#                  1! = 1

# 功能: 如果是不直接知道结果的数据, 就进行分解 9 9 * 8! 8 =
# 如果说, 直接知道结果的数据, 就直接返回 1! = 1
def jiecheng(n):
    if n == 1:
        return 1
    # n != 1
    return n * jiecheng(n - 1)

result = jiecheng(5)
print(result)