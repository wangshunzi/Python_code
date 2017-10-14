# _*_encoding:utf8_*_
#
#
# # 非原始字符串
# # 	使用单引号包含的
# # 		'abc'
# # str1 = 'aaa'
# # print(str1, type(str1))
#
#
# # 	使用双引号包含的
# # 		"abc"
# # str1 = "aaa"
# # print(str1, type(str1))
#
# # 	使用3个单引号
# # 		''' abc '''
# # str1 = '''aaa'''
# # print(str1, type(str1))
#
# # 	使用3个双引号
# # 		""" abc """
# # str1 = """aaa"""
# # print(str1, type(str1))
#
#
# # str1 = """a\taa"""
# # print(str1, type(str1))
#
#
#
# # 我是 "sz"
# # name = "我是 \'sz\'"
# # print(name)
#
# # name = "s"\
# # "z"\
# # "123"
# # print(name)
#
# # 我是 \n sz
# # name = r'''我是 \n \t \\ sz'''
# # print(name)
#
#
#
#
# # 我是 'sz'
# # name = "我是 \"sz\""
# # name = "我是 'sz'"
# # print(name)
#
#
# name = ("woshi"
# "sz")
# print(name)
#
#
#
# str1 = """woshi
# sz
# 123"""
# print(str1)
#
#
# import math
# math.sin(30)




# ----------------------字符串一般操作------------------------------

# result = "wangzha" + "shunzi"
# print(result)


# result = "wangzha"         "shunzi"
# print(result)


# result = "woshi%s, %d"%("123", 123)
# print(result)
#
#
# print("sz\t"*10)

# ----------------------字符串切片操作------------------------------


# name = "abcdefg"
#
# print(name[3])
# print(name)
#
#
# print(name[-4])
# # [0, 3)
# print(name[::])
# print(len(name))
# print(name[0:len(name):-1])
#
#
# print(name[4:1:-1])
# print(name[-1:-4:-1])



# ----------------------字符串函数操作------------------------------

# len
# 	作用
# 		计算字符串的字符个数
# 	语法
# 		len(name)
# 	参数
# 		字符串
# 	返回值
# 		整型
# 		字符个数
# name = "woshisz"
# name = "我\n是sz"
# num = len(name)
# print(num)





# find
# 	作用
# 		查找子串索引(下标)位置
# 	语法
# 		find(sub, start=0, end=len(str))
# 	参数
# 		参数1-sub
# 			需要检索的字符串
# 		参数2-start
# 			检索的起始位置
# 			可省略, 默认0
# 		参数3-end
# 			检索的结束位置
# 			可省略, 默认len(str)
# 	返回值
# 		找到了
# 			指定索引
# 			整型
# 		找不到
# 			-1
# 	注意
# 		从左到右进行查找
# 		找到后立即停止
#       [start, end)
# name = "wo shi sz"
# num = name.find("s", 4, 7)
# print(num)



# rfind
# 	功能使用, 同find
# 	区别
# 		从右往左进行查找
# name = "wo shi sz"
# num = name.rfind("s")
# print(num)




# index
# 	作用
# 		获取子串索引位置
# 	语法
# 		index(sub, start=0, end=len(str))
# 	参数
# 		参数1-sub
# 			需要检索的字符串
# 		参数2-start
# 			检索的起始位置
# 			可省略, 默认0
# 		参数3-end
# 			检索的结束位置
# 			可省略, 默认len(str)
# 	返回值
# 		找到了
# 			指定索引
# 			整型
# 		找不到
# 			异常
# 	注意
# 		从左到右进行查找
# 		找到后立即停止
# name = "wo shi sz"
# num = name.index("ss")
# print(num)




# rindex
# 	功能使用, 同index
# 	区别
# 		从右往左进行查找
# name = "wo shi sz"
# num = name.rindex("ss")
# print(num)



# count
# 	作用
# 		计算某个子字符串的出现个数
# 	语法
# 		count(sub, start=0, end=len(str))
# 	参数
# 		参数1-sub
# 			需要检索的字符串
# 		参数2-start
# 			检索的起始位置
# 			可省略, 默认0
# 		参数3-end
# 			检索的结束位置
# 			可省略, 默认len(str)
# 	返回值
# 		子字符串出现的个数
# 		整型
# name = "wo shi szwo"
# print(name.count("s"))



# ----------------------字符串函数转换操作------------------------------

#
# replace
# 	作用
# 		使用给定的新字符串 替换原字符串中的 旧字符串
# 	语法
# 		replace(old, new[, count])
# 	参数
# 		参数1-old
# 			需要被替换的旧字符串
# 		参数2-new
# 			替换后的新字符串
# 		参数3-count
# 			替换的个数
# 			可省略, 表示替换全部
# 	返回值
# 		替换后的结果字符串
# 	注意
# 		并不会修改原字符串本身
# name = "wo shi sz"
# # print(name.replace("s", "z"))
# print(name.replace("s", "z", 1))
# print(name)



# capitalize
# 	作用
# 		将字符串首字母变为大写
# 	语法
# 		capitalize()
# 	参数
# 		无
# 	返回值
# 		首字符大写后的新字符串
# 	注意
# 		并不会修改原字符串本身

# name = "wo shi sz"
# print(name.capitalize())
# print(name)


# title
# 	作用
# 		将字符串每个单词的首字母变为大写
# 	语法
# 		title()
# 	参数
# 		无
# 	返回值
# 		每个单词首字符大写后的新字符串
# 	注意
# 		并不会修改原字符串本身
# name = "wo shi-sz*sz2-qq%yy"
# print(name.title())
# print(name)



# lower
# 	作用
# 		将字符串每个字符都变为小写
# 	语法
# 		title()
# 	参数
# 		无
# 	返回值
# 		全部变为小写后的新字符串
# 	注意
# 		并不会修改原字符串本身
# name = "Wo Shi SZ"
# print(name.lower())
# print(name)



# upper
# 	作用
# 		将字符串每个字符都变为大写
# 	语法
# 		upper()
# 	参数
# 		无
# 	返回值
# 		全部变为大写后的新字符串
# 	注意
# 		并不会修改原字符串本身

# name = "Wo Shi SZ"
# print(name.upper())
# print(name)




# ----------------------字符串函数填充压缩操作------------------------------


# ljust
# 	作用
# 		根据指定字符(1个), 将原字符串填充够指定长度
# 		l
# 			表示原字符串靠左
# 	语法
# 		ljust(width, fillchar)
# 	参数
# 		参数1-width
# 			指定结果字符串的长度
# 		参数2-fillchar
# 			如果原字符串长度 < 指定长度时
# 			填充过去的字符
# 	返回值
# 		填充完毕的结果字符串
# 	注意
# 		不会修改原字符串
# 		填充字符的长度为1
# 		只有原字符串长度 < 指定结果长度时才会填充


# name = "abcdefg"
# print(name.ljust(16, "x"))
# print(name)




# rjust
# 	作用
# 		根据指定字符(1个), 将原字符串填充够指定长度
# 		r
# 			表示原字符串靠右
# 	语法
# 		rjust(width, fillchar)
# 	参数
# 		参数1-width
# 			指定结果字符串的长度
# 		参数2-fillchar
# 			如果原字符串长度 < 指定长度时
# 			填充过去的字符
# 	返回值
# 		填充完毕的结果字符串
# 	注意
# 		不会修改原字符串
# 		填充字符的长度为1
# 		只有原字符串长度 < 指定结果长度时才会填充
# name = "abcdefg"
# print(name.rjust(16, "x"))
# print(name)


# center
# 	作用
# 		根据指定字符(1个), 将原字符串填充够指定长度
# 		center
# 			表示原字符串居中
# 	语法
# 		center(width, fillchar)
# 	参数
# 		参数1-width
# 			指定结果字符串的长度
# 		参数2-fillchar
# 			如果原字符串长度 < 指定长度时
# 			填充过去的字符
# 	返回值
# 		填充完毕的结果字符串
# 	注意
# 		不会修改原字符串
# 		填充字符的长度为1
# 		只有原字符串长度 < 指定结果长度时才会填充
# name = "abcdefg"
# print(name.center(18, "x"))
# print(name)



# lstrip
# 	作用
# 		移除所有原字符串指定字符(默认为空白字符)
# 		l
# 			表示仅仅只移除左侧
# 	语法
# 		lstrip(chars)
# 	参数
# 		参数-chars
# 			需要移除的字符集
# 			表现形式为字符串
# 				"abc"
# 				表示,"a"|"b"|"c"
# 	返回值
# 		移除完毕的结果字符串
# 	注意
# 		不会修改原字符串

# name = "wwwoo shi sz "
# # print("|" + name.lstrip() + "|")
# print("|" + name.lstrip("wo") + "|")
# print("|" + name + "|")


# rstrip
# 	作用
# 		移除所有原字符串指定字符(默认为空白字符)
# 		r
# 			表示从右侧开始移除
# 	语法
# 		rstrip(chars)
# 	参数
# 		参数-chars
# 			需要移除的字符集
# 			表现形式为字符串
# 				"abc"
# 				表示,"a"|"b"|"c"
# 	返回值
# 		移除完毕的结果字符串
# 	注意
# 		不会修改原字符串
# name = "wwwoo shi sz oowwwoa"
# # print("|" + name.lstrip() + "|")
# print("|" + name.rstrip("wo") + "|")
# print("|" + name + "|")

# ----------------------字符串函数分割拼接操作------------------------------

# split
# 	作用
# 		将一个大的字符串分割成几个子字符串
# 	语法
# 		split(sep, maxsplit)
# 	参数
# 		参数1-sep
# 			分隔符
# 		参数2-maxsplit
# 			最大的分割次数
# 			可省略, 有多少分割多少
# 	返回值
# 		分割后的子字符串, 组成的列表
# 		list 列表类型
# 	注意
# 		并不会修改原字符串本身

# info = "sz-18-180-0558-12345678"
# result = info.split("-", 3)
# print(result)
# print(info)


# partition
# 	作用
# 		根据指定的分隔符, 返回(分隔符左侧内容, 分隔符, 分隔符右侧内容)
# 	语法
# 		partition(sep)
# 	参数
# 		参数-sep
# 			分隔符
# 	返回值
# 		如果查找到分隔符
# 			(分隔符左侧内容, 分隔符, 分隔符右侧内容)
# 			tuple 类型
# 		如果没有查找到分隔符
# 			(原字符串, "", "")
# 			tuple 类型
# 	注意
# 		不会修改原字符串
# 		从左侧开始查找分隔符
# info = "sz-18-180-0558-12345678"
# result = info.partition("-")
# print(result)
# print(info)



# rpartition
# 	作用
# 		根据指定的分隔符, 返回(分隔符左侧内容, 分隔符, 分隔符右侧内容)
# 		r
# 			表示从右侧开始查找分隔符
# 	语法
# 		partition(sep)
# 	参数
# 		参数-sep
# 			分隔符
# 	返回值
# 		如果查找到分隔符
# 			(分隔符左侧内容, 分隔符, 分隔符右侧内容)
# 			tuple 类型
# 		如果没有查找到分隔符
# 			(原字符串, "", "")
# 			tuple 类型
# 	注意
# 		不会修改原字符串
# 		从右侧开始查找分隔符

# info = "sz-18-180-0558-12345678"
# result = info.rpartition("-")
# print(result)
# print(info)


# splitlines
# 	作用
# 		按照换行符(\r, \n), 将字符串拆成多个元素, 保存到列表中
# 	语法
# 		splitlines(keepends)
# 	参数
# 		参数-keepends
# 			是否保留换行符
# 			bool 类型
# 	返回值
# 		被换行符分割的多个字符串, 作为元素组成的列表
# 		list 类型
# 	注意
# 		不会修改原字符串
# name = "wo \n shi \r sz"
# result = name.splitlines(True)
# print(result)
# print(name)




# join
# 	作用
# 		根据指定字符串, 将给定的可迭代对象, 进行拼接, 得到拼接后的字符串
# 	语法
# 		join(iterable)
# 	参数
# 		iterable
# 			可迭代的对象
# 				字符串
# 				元组
# 				列表
# 				...
# 	返回值
# 		拼接好的新字符串

# items = ["sz", "18", "shanghai"]
# result = "xxx".join(items)
# print(result)

# ----------------------字符串函数判定操作------------------------------



#
# isalpha
# 	作用
# 		字符串中是否所有的字符都是字母
# 			不包含该数字,特殊符号,标点符号等等
# 			至少有一个字符
# 	语法
# 		isalpha()
# 	参数
# 		无
# 	返回值
# 		是否全是字母
# 		bool 类型

# name = "Sz\t"
# name = ""
# print(name.isalpha())


# isdigit
# 	作用
# 		字符串中是否所有的字符都是数字
# 			不包含该字母,特殊符号,标点符号等等
# 			至少有一个字符
# 	语法
# 		isdigit()
# 	参数
# 		无
# 	返回值
# 		是否全是数字
# 		bool 类型
# name = "123\t"
# name = ""
# print(name.isdigit())


# isalnum
# 	作用
# 		字符串中是否所有的字符都是数字或者字母
# 			不包含该特殊符号,标点符号等等
# 			至少有一个字符
# 	语法
# 		isalnum()
# 	参数
# 		无
# 	返回值
# 		是否全是数字或者字母
# 		bool 类型
# name = "123abc,"
# print(name.isalnum())


# isspace
# 	作用
# 		字符串中是否所有的字符都是空白符
# 			包括空格,缩进,换行等不可见转义符
# 			至少有一个字符
# 	语法
# 		isspace()
# 	参数
# 		无
# 	返回值
# 		是否全是空白符
# 		bool 类型
# name = "\n"
# print(name.isspace())


# startswith
# 	作用
# 		判定一个字符串是否以某个前缀开头
# 	语法
# 		startswith(prefix, start=0, end=len(str))
# 	参数
# 		参数1-prefix
# 			需要判定的前缀字符串
# 		参数2-start
# 			判定起始位置
# 		参数3-end
# 			判定结束位置
# 	返回值
# 		是否以指定前缀开头
# 		bool 类型
# name = "2018-09-02: 某某报告.xls"
# print(name.startswith("18", 2, 4))



# endswith
# 	作用
# 		判定一个字符串是否以某个后缀结尾
# 	语法
# 		endswith(suffix, start=0, end=len(str))
# 	参数
# 		参数1-suffix
# 			需要判定的后缀字符串
# 		参数2-start
# 			判定起始位置
# 		参数3-end
# 			判定结束位置
# 	返回值
# 		是否以指定后缀结尾
# 		bool 类型
# name = "2018-09-02: 某某报告.xls"
# name = "2018-09-02: 某某报告.doc"
# print(name.endswith(".doc"))


# 补充
# 	in
# 		判定一个字符串, 是否被另外一个字符串包含
# 	not in
# 		判定一个字符串, 是否不被另外一个字符串包含

print("sz" in "wo shi z")
print("sz" not in "wo shi z")





name = "abc"
name[0] = "d"
print(name[0])









