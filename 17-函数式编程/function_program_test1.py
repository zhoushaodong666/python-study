# 匿名函数
"""
语法：
lambda parameter_list:expression
"""
def add(x,y):
    return x+y

f = lambda x,y: x+y


print(add(1,2))  # 3
print(f(1,2))  # 3

# lambda表达式中只能写表达式，不能写语句
# f = lambda x,y: a = x+y