# open()方法第2个参数传入写入模式 （ 'w' ），可以创建一个空文件

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

