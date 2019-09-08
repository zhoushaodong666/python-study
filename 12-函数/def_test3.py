# 多个返回值接收涉及的是【序列封包】和【序列解包】
# 序列可以是 【列表，字符串，元组，字典，集合】等序列
a, b, c = 1, 2, 3
print(a, b, c)  # 1 2 3

# 将a b c三个变量全部放进一个元组d中 这就是【序列封包】
d = a, b, c
print(d)  # (1, 2, 3)
print(type(d))  # <class 'tuple'>

# 将元组d赋值给a2 b2 c2三个变量 这就是【序列解包】
a2,b2,c2 = d
print(a2,b2,c2)  # 1 2 3
print(type(a2))  # <class 'int'>
print(type(b2))  # <class 'int'>
print(type(c2))  # <class 'int'>

# 字典
a3,b3 = {a:1,b:2}
print(a3)  # 1

# set集合
a4,b4 = {1,2}
print(a4,b4)  # 1 2


# list列表
a5,b5 = [1,2]
print(a5,b5)  # 1 2

# 字符串
a6,b6,c6,d6,e6 = "hello"
print(a6,b6,c6,d6,e6)  # h e l l o
