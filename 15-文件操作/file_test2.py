# open()方法第2个参数传入写入模式 ('w')，可以创建一个空文件

# 1.文件写入空文件
# 根据相对路径，15-文件操作这个文件夹下将会创建一个programming_write_to1.txt的文件
# 内容：
# I Love China
filename1 = "programming_write_to1.txt"
with open(filename1,"w") as fileObject1:
    fileObject1.write("I Love China")


# 2.写入多行
# 根据相对路径，15-文件操作这个文件夹下将会创建一个programming_write_to1.txt的文件
# 内容：
# I Love China.
# China will better and  better.
filename2 = "programming_write_to2.txt"
with open(filename2,"w") as fileObject2:
    # 这样写发现文件内容为：I Love China.China will better and  better.
    # 每一句没有独占一行
    #fileObject2.write("I Love China.")
    #fileObject2.write("China will better and  better.")

    # 正确的换行 在内容尾部加入"\n"
    fileObject2.write("I Love China.\n")
    fileObject2.write("China will better and  better.\n")


# 3.追加内容到文件
# 如果你要给文件添加内容，而不是覆盖原有的内容，可以 附加模式("a")打开文件。
# 如果使用写入模式("w"),会重新创建一个空文件写入，并不是在原文件基本上追加内容
filename3 = "programming_write_to2.txt"
with open(filename3,"a") as fileObject3:
    fileObject3.write("I am append content.\n")
#  发现programming_write_to2.txt的内容追加一行：I am append content.
# I Love China.
# China will better and  better.
# I am append content.

