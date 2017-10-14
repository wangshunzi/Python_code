
import os

# file_list = os.listdir("files")
# print(file_list)

# 通过给定的文件夹, 列举出这个文件夹当中, 所有的文件,以及文件夹, 子文件夹当中的所有文件
def listFilesToTxt(dir, file):
    # 1. 列举出, 当前给定的文件夹, 下的所有子文件夹, 以及子文件
    file_list = os.listdir(dir)
    # print(file_list)
    # 2. 针对于, 列举的列表, 进行遍历
    for file_name in file_list:
        new_fileName = dir + "/" + file_name
        # 判定, 是否是目录, listFiles
        if os.path.isdir(new_fileName):
            # print(new_fileName)
            file.write(new_fileName + "\n")
            listFilesToTxt(new_fileName, file)
        else:
             # 打印下, 文件名称
            # print("\t" + file_name)
            file.write("\t" + file_name + "\n")
    # print("")
    file.write("\n")

f = open("list.txt", "a")
listFilesToTxt("files", f)

