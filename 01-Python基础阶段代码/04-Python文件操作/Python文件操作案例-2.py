

# # 0, 获取所有的文件名称列表
# import os
# import shutil
#
# path = "files2"
#
# if not os.path.exists(path):
#     exit()
#
# os.chdir(path)
# file_list = os.listdir("./")
# # print(file_list)
#
# # 1. 遍历所有的文件(名称)
# for file_name in file_list:
#     # print(file_name)
#     # 2. 分解文件的后缀名
#     # 2.1 获取最后一个.的索引位置 xx.oo.txt
#     index = file_name.rfind(".")
#     if index == -1:
#         continue
#     # print(index)
#     # 2.2 根据这个索引位置, 当做起始位置, 来截取后续的所有字符串内容
#     extension = file_name[index + 1:]
#     print(extension)
#
#     # 3. 查看一下, 是否存在同名的目录
#
#     # 4. 如果不存在这样的目录 -> 直接创建一个这样名称的目录
#     if not os.path.exists(extension):
#         os.mkdir(extension)
#
#     shutil.move(file_name, extension)
#
#     # 5, 目录存在 -> 移动过去
#
#     # 创建 移动 移动




