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

# 数字的几种机制表示方法
# 常见的 10机制 2进制 8进制 16进制
# 10进制
print(5) # 5

# 2进制 例如0b11 0b/0B 表示二进制 11为二进制的数组大小
print(0b11) # 3

# 8进制 0o/0O 表示八进制
print(0o10) # 8

# 16进制 0x/0X 表示十六进制
print(0x10) # 16

# 进制转换
# bin 将其他进制转化为二进制
print(bin(10)) # 0b1010
print(bin(0o5)) # 0b101
print(bin(0xF)) # 0b1111

# int 将其他进制转化为十进制
print(int(0b10)) # 2
print(int(0O10)) # 8
print(int(0x10)) # 16

# oct 将其他进制转化为八进制
print(oct(10)) # 0o12
print(oct(0b10)) # 0o2
print(oct(0x10)) # 0o20

# hex 将其他进制转化为十六进制
print(hex(666)) # 0x29a
print(hex(0b1010)) # 0xa
print(hex(0o777)) # 0x1ff


