
# Python版本的问题
# 思路, 语法 -> 工具
# Python3.x



# 使用注释, 理清楚, 具体的实现步骤
# 代码填充


# 输入
# 	身高
personHeight = input("请输入身高(m):")
personHeight = float(personHeight)

# 	体重
personWeight = input("请输入体重(kg):")
personWeight = float(personWeight)

# 	年龄
personAge = input("请输入年龄:")
personAge = int(personAge)

# 	性别
personSex = input("请输入性别（男：1 女：0）:")
personSex = int(personSex)



# 处理数据
# 	计算体脂率
# BMI = 体重（kg） / （身高 * 身高）（米）
# 体脂率 = 1.2 * BMI + 0.23 * 年龄 - 5.4 - 10.8*性别（
BMI = personWeight / (personHeight * personHeight)
TZL = 1.2 * BMI + 0.23 * personAge - 5.4 - 18.8 * personSex


# 	判定体脂率, 是否在正常的标准范围之内
# 正常成年人的体脂率分别是男性15%~18%和女性25%~28%

# TZL  MIN  MAX
# 0.10 1 0
minNum = 0.15 + 0.10 * (1 - personSex)
maxNum = 0.18 + 0.10 * (1 - personSex)

result = minNum < TZL < maxNum


# 输出
# 	告诉用户, 是否正常
print("你的体脂率, 是%f" % TZL)
print("你的体脂率, 是否符合标准", result)