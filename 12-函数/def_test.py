# 函数的定义
# 使用def语句
# 格式：
# def 函数名（参数列表）:
#     函数体

# 定义一个函数 函数允许有return返回值 如果没有默认返回None
def funcname(parm):
    pass


# 函数调用

# 如果函数调用在函数定义之前 程序会报错：NameError: name 'printHelloWorld' is not defined
# python是解释性的语言 会按照先后循环进行编译
# 函数调用一定要在函数定义之后
# printHelloWorld()

def printHelloWorld():
    print("HelloWorld")


printHelloWorld()  # HelloWorld


# 定义一个含有返回值的函数
def add(x, y):
    return x + y


result = add(10,20)
print(result) # 30
