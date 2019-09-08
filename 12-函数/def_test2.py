# 定义一个含有返回值的函数
def add(x, y):
    return x + y


result = add(10,20)
print(result)  # 30

# 定义一个含有多个返回值的函数
# 将传入的a和b都乘以3 并返回
def threeMultiple(a,b):
    return a*3,b*3

# 使用一个变量接收函数的多个返回值
# 一个变量接收多个变量 python会将返回值都放进一个元组内返回
# 不推荐 使用这种方式接收多个函数返回值 因为使用元组序列去访问元素，当返回值数量过多时，难以分清每个元素的含义。
totalResult = threeMultiple(10,20)
print(totalResult)  # (30, 60)
print(totalResult[0],totalResult[1])  # 30 60
print(type(totalResult))  # <class 'tuple'>

# 使用多个变量接收返回值(接收变量数和函数返回值数量一致)
# 推荐 容易分清每个元素的含义
result1,result2 = threeMultiple(10,20)
print(result1,result2) # 30 60



