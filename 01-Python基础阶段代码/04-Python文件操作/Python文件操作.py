



# 1. 打开文件

# 相对路径, 相对于哪一个目录下面的指定文件
# f = open("a.txt", "r+")
#
# # 2. 读写操作
# content = f.read()
# print(content)
# #
# f.write("88888")
#
#
# # 3. 关闭文件
# f.close()




# 1. 打开xx.jpg文件, 取出内容, 获取内容的前面半部分
# 1.1 打开文件
# fromFile = open("xx.jpg", "rb")
#
# # 1.2 读取文件内容
# fromContent = fromFile.read()
# print(fromContent)
#
# # 1.3 关闭文件
# fromFile.close()
#
#
# # 2. 打开另外一个文件xx2.jpg, 然后, 把取出的半部分内容, 写入到xx2.jpg文件里面去
# # 2.1 打开目标文件
# toFile = open("xx2.jpg", "wb")
#
# # 2.2 写入操作
# content = fromContent[0: len(fromContent) // 2]
# toFile.write(content)
#
#
# # 2.3 关闭文件
# toFile.close()



# f = open("a.txt", "rb")
#
# print(f.tell())
# f.seek(-2, 2)
# print(f.tell())
#
# print(f.read())
# print(f.tell())
#
#
#
# f.close()

# f = open("a.txt", "r")

# f.read(字节数)
# 	字节数默认是文件内容长度
# 	下标会自动后移e
# f.seek(2)
# content = f.read(2)
# print(f.tell())
# print(content)



# f.readline([limit])
# 	读取一行数据
# 	limit
# 		限制的最大字节数
# print("----", f.tell())
# content = f.readline()
# print(content, end="")
# print("----", f.tell())
#
#
#
# content = f.readline()
# print(content, end="")
#
#
# print("----", f.tell())
#
# content = f.readline()
# print(content, end="")
#
# print("----", f.tell())



# f.readlines()
# 	会自动的将文件按换行符进行处理
# 	将处理好的每一行组成一个列表返回

# content = f.readlines()
# print(content)
#
#
# f.close()


import collections


# f = open("a.txt", "r")

# print(isinstance(f, collections.Iterator))
#
# for i in f:
#     print(i, end="")
#
# if f.readable():
#     content = f.readlines()
#     for i in content:
#         print(i, end="")

# f.close()

# f = open("a.txt", "r")
#
# if f.writable():
#     print(f.write("abc"))
#
#
# f.close()



f = open("a.txt", "w")


f.write("123")


f.flush()

f.close()

















