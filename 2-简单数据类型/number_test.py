# 数字 :整形与浮点型

# 整形 type(数据类型) type函数可以根据传入的参数 判断数据类型是什么
print(type(1)) # <class 'int'>

# 浮点型 带小数点的 精度比整形大
print(type(1.0)) # <class 'float'>

# 整形+浮点型 = 浮点型
print(type(1+1.0)) # <class 'float'>

# 整形*整形 = 整形
print(type(1*1)) # <class 'int'>

# 浮点型*浮点型 = 浮点型
print(type(1.0*1.0)) # <class 'float'>

# 整形*浮点型 = 浮点型
print(type(1*1.0)) # <class 'float'>

# 整形/浮点型 = 浮点型  浮点型/整形 = 浮点型
print(type(1/1.0)) # <class 'float'>
print(type(1.0/1)) # <class 'float'>

# 整形/整形 = 浮点型 单斜杠"/"除法会将整形自动转换为浮点型
print(type(1/1)) # <class 'float'>
print(1/1) # 1.0

# 整形//整形 = 整形  双斜杠"//"除法会将整形除法结果取整
print(type(1//1)) # <class 'int'>
print(1//1) # 1

# 1/2=0.5 取整就是0了
print(1//2) # 0

