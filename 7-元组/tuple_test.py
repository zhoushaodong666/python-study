# 元组
# 元组的定义
# Python的元组与列表类似，不同之处在于元组的元素不能修改。
# 元组使用小括号，列表使用方括号。
# 元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
tuple1 = ()  # 定义一个空元组
print(tuple1)  # ()


# (1)和(1)python既可以认为是int类型的数字1，也可以认为是一个元素的元组
# 所以在定义只含有一个元素的元组,一个元素也要在后面加上逗号，这样python编译器才会识别为元组
print(type(1))  # <class 'int'>
tuple2 = (1,)   # <class 'tuple'>

print(type(tuple2))  # <class 'tuple'>


tuple3 = (1, 2, 3)  # 定义含有多个元素的元组
print(tuple3)  # (1, 2, 3)

# 元组元素的访问
# 通过索引下标来访问元组中的元素
tuple4 = ("a", "b", "c")
print(tuple4[0])  # a
print(tuple4[0:])  # ('a', 'b', 'c')
print(tuple4[0:2])  # ('a', 'b')

# 元组的修改
# 元组的修改只能通过重新赋值的方式
tuple5 = ('nice', 'to', 'meet', 'you')
print(tuple5)  # ('nice', 'to', 'meet', 'you')

#元组的元素不允许修改
#tuple5[0]='a' TypeError: 'tuple' object does not support item assignment

tuple5 = ('hello','every','body')
print(tuple5)  # ('hello', 'every', 'body')

# 元组的删除
# 元组的元素时不允许删除的，只能删除整个元组
tuple6 = (1,'5','a')
print(tuple6)  # (1, '5', 'a')
del tuple6 # 删除元组tuple6

# NameError: name 'tuple6' is not defined
#print("删除后的tuple6："+tuple6)

# 元组运算符
# 计算元组的长度 使用len()函数
tuple7 = (1, 5, 654, 6, 54)
length = len(tuple7)
print(length)  # 5

# 元组的连接 使用"+"号
print((1, 2, 3)+(4, 5, 6))   # (1, 2, 3, 4, 5, 6)

# 元组的重复 使用 "*"号
print(('hello', )*3)  # ('hello', 'hello', 'hello')

# 判断某个值是否存在于元组中 使用 "in" 关键字
print(3 in (1, 2, 3))  # True

# 判断某个值是否不存在于元组中 使用 "not in" 关键字
print(4 not in (1, 2, 3))  # True

# 迭代遍历元组
for x in (1, 2, 3):
    print(x)  # 1 2 3
