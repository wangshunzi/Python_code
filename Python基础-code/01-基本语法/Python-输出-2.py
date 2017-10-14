# _*_coding:utf-8 _*_
# 输出一个值
print 123


# 输出一个变量
num = 10
print num

# 输出多个变量
num2 = 66
print num, num2


# 格式化输出
#
name = "sz"
age = 18

# 我的名字是xxx, 年龄是xxx
print "我的名字是", name, ", 年龄是", age

newStr = "我的名字是%s, 年龄是%d"%(name, age)

print newStr

print "我的名字是{0}, 年龄是{0}".format(name, age)


# 输出到文件中
f = open("test.txt", "w")
print >>f, "xxxxxxxxx"


print "1",
print "2",
print "3",


# 输出的各个数据, 使用分隔符分割

print "a","-", "b","-", "c"
print "-".join(["a", "b", "c"])
