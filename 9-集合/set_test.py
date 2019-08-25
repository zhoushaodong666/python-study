


# Set集合是一个无序的不重复元素序列。
# set集合的创建
# 方式1 通过 {value1,value2,..}创建
set1 = {1, 2, 3, 1, 2}
print(set1)  # {1, 2, 3}
print(type(set1))  # <class 'set'>
# 结论1 set集合是不存在重复元素的

# 方式2 通过set()函数创建
set2 = set('123456')
print(type(set2))  # <class 'set'>
print(set2)
# 第1次运行输出结果： {'4', '6', '3', '5', '1', '2'}
# 第2次运行输出结果： {'6', '4', '2', '1', '5', '3'}
# 结论2 set集合是无序的，每次输出的结果顺序都可能不同

# 从结论1和2可以知道Set集合是一个无序的不重复元素序列。

# 如何创建一个空的set集合
# 使用方式1 {} 创建的是一个空字典 不是一个空集合
print(type({}))  # <class 'dict'>

# 使用方式2 set()函数创建 可以创建一个空集合
print(type(set()))  # <class 'set'>

# set集合添加元素
# 通过add()方法
set3 = {1,2,3}
print(set3)  # {1, 2, 3}
set3.add(4) # set3添加一个值为4的元素
print(set3)  # {1, 2, 3, 4}

# 通过update()方法 且参数可以是列表，元组，字典等
set4 = {1, 2, 3}
print(set3)
# 添加不可迭代的数据类型
#set4.update(6) # TypeError: 'int' object is not iterable

# 添加可迭代的数据类型
# 添加列表
set4.update([1, 4, 5])
print(set4)  # {1, 2, 3, 4, 5}

# 添加元组
set4.update((1, 6, 7))
print(set4)  # {1, 2, 3, 4, 5, 6, 7}

# 添加字典 只添加字典的键名 键值不添加进集合中
set4.update({"a": 8,"c":9})
print(set4)  # {1, 2, 3, 4, 5, 6, 7, 'c', 'a'}

# set集合元素的移除
# 1.通过remove()方法 移除不存在的元素 程序会报错
set5 = {1, 2, 3}
print(set5)  # {1, 2, 3}
set5.remove(1)
print(set5)  # {2, 3}

#set5.remove("a")  # TypeError: descriptor 'remove' requires a 'set' object but received a 'str'

# 2.通过discard()方法 移除不存在的元素 程序不会报错
set6 = {1, 2, 3}
set6.discard('a')

# 3.通过pop()方法 随机删除一个set集合中的元素
set7 = {1, 2, 3}
val = set7.pop()
print(val) # 1
print(set7)  # {2, 3}

# 获取set集合元素个数
set8 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(len(set8))  # 9

# 清空集合 通过clear()方法
set9 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(set9)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}
set9.clear()
print(set9)  # set()

# 判断元素是否在set集合中
set10 = {1,2,3}
print(set10)
print(1 in set10)  # True
print(10 in set10)  # False