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
# 使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。

def printName(a,b):
    print(a,b)


# 一般方式调用
printName("小白","小丽")  # 小白 小丽

# 关键字参数调用
# 可以看到 先输入小白 却后面输出，因为b ="小白”,b是函数的第二个参数,a = "小丽"，a是函数的一个参数
# 所以相当于 printName("小丽","小白")
printName(b = "小白",a = "小丽")  # 小丽 小白


# 3.默认参数