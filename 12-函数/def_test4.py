# 函数参数
# 1.必须参数 必需参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。

def add(x,y):
    print("add函数必须传入2个参数才能调用")

# 错误示例 少传入一个参数
#add(1)  # TypeError: add() missing 1 required positional argument: 'y'

# 正确示例
add(1,2)  # add函数必须传入2个参数才能调用

# 2.关键字参数
# 关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。
# 使用关键字参数允许函数调用时参数的【顺序与声明时不一致】，因为 Python 解释器能够用参数名匹配参数值。

def printName(a,b):
    print(a,b)


# 一般方式调用
printName("小白","小丽")  # 小白 小丽

# 关键字参数调用
# 可以看到 先输入小白 却后面输出，因为b ="小白”,b是函数的第二个参数,a = "小丽"，a是函数的一个参数
# 所以相当于 printName("小丽","小白")
printName(b = "小白",a = "小丽")  # 小丽 小白


# 3.默认参数
# 调用函数时，如果没有传递参数，则会使用默认参数

# name没有默认值，所以必传。age=18有默认值，当外部实参不传递age值时，默认age=18
def printStudent(name,age=18):
    printName("姓名：",name)
    printName("年龄：",age)

printStudent("库里")
print("=====================")
printStudent("卡特",28)

#输出结果

# 姓名： 库里
# 年龄： 18
# =====================
# 姓名： 卡特
# 年龄： 28

# 4.不定长参数
# 你可能需要一个函数能处理比当初声明时更多的参数
# 加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数
def manyParam(arg1,*tuple_args):
    print(arg1)
    print(tuple_args)
    print(type(tuple_args))

manyParam(1,2,3,4,5)
# 除了第1个args变量有命名，其他2-5参数未命名，则全部放进不定长参数tuple_args中，这是一个元组
# 输出结果
# 1
# (2, 3, 4, 5)
# <class 'tuple'>