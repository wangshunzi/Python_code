#
# 反转字符串
# 	源字符串
# 		"社会我顺哥, 人狠话不多"
# 	反转后
# 		"多不话狠人 ,哥顺我会社"


notice = "社会我顺哥, 人狠话不多"

# 拆字
result = ""
for c in notice:
    # result += c # result = result + c
    result = c + result
    # print(c)
print(result)