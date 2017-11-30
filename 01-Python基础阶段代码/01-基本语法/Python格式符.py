

# 格式化输出
name = "sz"
age = 18

# 我的名字是xxx, 年龄是xxx
print("我的名字是%s, 年龄是%d"%(name, age))


# %[(name)][flags][width][.precision]typecode
# []: 可以省略

# (name)
# 表示, 根据, 制定的名称(key), 查找对应的值, 格式化到字符串当中
mathScore = 59
englishScore = 58
# print("我的数学分数是%d, 英文的分数是: %d"%(mathScore, englishScore))
# print("我的数学分数是%d, 英文的分数是: %d"%(englishScore, mathScore))
# print("我的数学分数是%(ms)d, 英文的分数是: %(es)d"%({"es": englishScore, "ms": mathScore}))

# width , 表示, 占用的宽度
# print("%-10d" % mathScore)
# print("%  d" % mathScore)


# min = 5
# sec = 18
# # 05:08
# print("%12d:%02d"%(min, sec))

score = 59.9

# print("%.2f"%score)
# print("%i"%score)

# print("%d" % 0x10)

# print("%o" % 10)
#
#
# print("%E"%15555555)


print("%g"%1011111)



# print("%s"%"abc")

print("%c" % 19997)


# 99%
print("99%")
score = 65
print("%d%%"%score)

# print("%b"%123)