# open()方法
# python中的文件操作依靠的 open()方法，通过传入不同的参数，可以有很多种文件操作方式
# 注意：使用 open() 方法一定要保证关闭文件对象，即调用 close() 方法。
"""
语法格式：
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
参数说明:

file: 必需，文件路径（相对或者绝对路径）。
mode: 可选，文件打开模式
buffering: 设置缓冲
encoding: 一般使用utf8
errors: 报错级别
newline: 区分换行符
closefd: 传入的file参数类型
opener:
"""

# 1.读取整个文件
# 我在【15-文件操作】的目录下创建一个名为file1.txt的文本文件
# 我在【15-文件操作】文件夹下创建的py文件，所以python会在这个【15-文件操作】文件夹下找file1.txt

# 方式1：完整写法
# 【不推荐】
file1 = open("file1.txt","r")
content1 = file1.read()
print(content1) # I am a file
file1.close()

# 方式2：不传读取模式参数"r"
# 省略open()方法第2个参数，因为参数默认是"r"
# 【不推荐】
file2 = open("file1.txt")
content2 = file2.read()
print(content2) # I am a file
file2.close()

# 方式3：不传读取模式参数"r" 与使用 with ... as 自动关闭文件对象
# 【推荐】
# 原因：我们调用了 open() ，但没有调用 close() ；你也可以调用 open() 和 close() 来打开和关闭文件。
# 但这样做时，如果程序存在 bug ，导致 close() 语句未执行，文件将不会关闭。
# 这看似微不足道，但未妥善地关闭文件可能会导致数据丢失或受损。如果在程序中过早地调用 close() ，
# 你会发现需要使用文件时它已 关闭 （无法访问），这会导致更多的错误。
# 并非在任何情况下都能轻松确定关闭文件的恰当时机，但通过使用前面所示的结构，
# 可让 Python 去确定：你只管打开文件，并在需要时使用它， Python 自会在合适的时候自动将其关闭。
with open("file1.txt") as file3:
    content3 = file3.read()
    print(content3) # I am a file


# 2.读取子文件夹下的文件
# 【相对路径】：相对于执行程序文件的目录
# 我运行的是15-文件操作文件夹下的py文件，所以【相对路径】就为 file_child/file2.txt
with open("file_child/file2.txt") as file4:
    content4 = file4.read()
    print(content4)  # I am file_child/file2.txt

# 【绝对路径】：带有盘符的全路径
# E:/Coding/pycharm_project/python-study/15-文件操作/file_child/file2.txt 就是我文件的全路径
all_path = "E:/Coding/pycharm_project/python-study/15-文件操作/file_child/file2.txt"
with open(all_path) as file5:
    content5 = file5.read()
    print(content5)

# 3.逐行读取文件内容

with open("file3.txt") as file6:
    for line_content in file6:
        #print(line_content) 输出内容有空白行隔开 因为文件一个换行符，print()一个换行符
        # 要消除这些多余的空白行，可在 print 语句中使用 rstrip()
        print(line_content.rstrip())





