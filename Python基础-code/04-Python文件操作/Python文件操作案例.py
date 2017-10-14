#
# import os
#
# os.chdir("files")
#
# # 1. 只读模式, 打开要复制的文件
# # 	追加模式, 打开副本文件
#
# source_file = open("d.txt", "r", encoding="utf-8")
# dst_file = open("d_bat.txt", "a", encoding="utf-8")
#
#
#
# # 2. 从源文件中读取内容
# # 	写入到目标文件中
# # content = source_file.read()
# # dst_file.write(content)
#
# while True:
#     content = source_file.read(1024)
#     if len(content) == 0:
#         break
#     print("----", content)
#     dst_file.write(content)
#
#
# # 3. 关闭源文件和目标文件
# source_file.close()
# dst_file.close()





















# 0, 获取所有的文件名称列表
# import os
# import shutil
#
#
# os.chdir("files")
# file_list = os.listdir("./")
# # print(file_list)
#
# # 1. 遍历所有的文件(名称)
# for file_name in file_list:
#     # print(file_name)
#     # 2. 分解文件的后缀名
#     # 2.1 获取最后一个.的索引位置 xx.oo.txt
#     index = file_name.rfind(".")
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

import os
def listAllFileToTxt(path, toFile):
    file_list = os.listdir(path)
    for file_name in file_list:
        if os.path.isdir(path + "/" + file_name):

            # print(path + "/" + file_name)
            toFile.write(path + "/" + file_name + "\n")
            listAllFileToTxt(path + "/" + file_name, toFile)
        else:
            # print("\t" + file_name)
            toFile.write("\t" + file_name + "\n")

    # print("")
    toFile.write("\n")

f = open("list.txt", "a")
listAllFileToTxt("files", f)
