# 第9章 文件
# 打开文件
# open(file, mode = 'r', buffering = -1)

# 标准文件：
# sys模式中定义了3个标准文件：stdin, stdout, stderr
import sys
f = sys.stdout
f.write("hello\n")

# 文件的读写
# 写文件：write(str)
# 读文件：read(), readline(), readlines()
# tell()方法可以获取文件当前的读写位置
# seek(offset, from)控制文件的读写位置，offset表示偏移量，from用于指定起始位置0-文件开头，1-当前位置，2-文件末尾
file = open('喜欢你.txt', encoding='utf-8')
print("文件编码：%s"%file.encoding)
print("文件名：%s"%file.name)
print(file.read())
file.close()

# os模块：import os
# 文件重命名：os.rename("a.txt", "b.txt")
# 删除文件：os.remove("b.txt")
# 创建文件夹：os.mkdir("dir")
# 删除文件夹：os.rmdir("dir")
# 获取当前目录：os.getcwd()
# 更改默认目录：os.chdir("E:\\")
# 获取目录列表：os.listdir("./")