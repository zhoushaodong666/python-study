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