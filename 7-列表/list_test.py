# 1.列表:由一系列按特定顺序排列的元素组成。
# 你可以创建包含字母表中所有字母、数字0~9或所有家庭成员姓名的列表；
# 也可以将任何东西加入列表中，其中的元素之间可以没有任何关系。
# 在Python中，用方括号（ [] ）来表示列表，并用逗号来分隔其中的元素。

# example1 列表内元素都是同一种数据类型
print([1, 2, 3, 4])  # [1, 2, 3, 4]
print(type([1, 2, 3, 4]))  # <class 'list'>

# example2 列表内元素不是同一种数据类型
print([1, 2, "hello", "world"])  # [1, 2, 'hello', 'world']
print(type([1, 2, "hello", "world"]))  # <class 'list'>

# example3 列表内嵌套列表 类似其它语言的多维数组的概念
print(
    [[1, 2], ["hello", "world"], [True, False], [1.0, 2.0]])  # [[1, 2], ['hello', 'world'], [True, False], [1.0, 2.0]]
print(type([[1, 2], ["hello", "world"], [True, False], [1.0, 2.0]]))  # <class 'list'>

# 2.列表元素的访问 通过下标访问列表元素 下标从0开始 最大下标是列表长度减1
# example4
list1 = ["nice", "to", "meet", "you"]
print(list1[0])  # nice
print(list1[3])  # you

# list1的长度是4 最大下标应该是3 我们访问4 超过了最大下标 会报错显示下标越界 IndexError: list index out of range
print(len(list1))  # 4
# print(list1[4])

# 3.列表元素的修改、添加、删除
# example5
# 修改
list2 = ["put", "you", "hand", "up"]
print(list2)  # ['put', 'you', 'hand', 'up']
list2[3] = "down"  # 将list2下标为3的元素的值修改为down
print(list2)  # ['put', 'you', 'hand', 'down']

# 添加
# 末尾添加新元素
list3 = ["hello", "every", "body"]
print(list3) #  ['hello', 'every', 'body']
list3.append("good")  # 向list3的末尾添加值为good的元素
print(list3)  # ['hello', 'every', 'body', 'good']

# 指定索引下标插入新元素
list4 = ["I", "Love", "you"]
print(list4)  # ['I', 'Love', 'you']
list4.insert(2, "bad")  # 使用insert函数可以想该列表的任何位置插入新元素，你需要传入指定的下标和值
print(list4)  # ['I', 'Love', 'bad', 'you']

list4.insert(20, "my")  # 传入下标超过最大下标值 默认使用最大下标 插入列表末尾
print(list4)  # ['I', 'Love', 'bad', 'you', 'my']

list4.insert(-1, "boy")  # 传入的下标也允许使用负数的
print(list4)  # ['I', 'Love', 'bad', 'you', 'boy', 'my']

# 删除
# 使用del语句删除元素
list5 = ["what", "are", "you", "doing", "?"]
print(list5)  # ['what', 'are', 'you', 'doing', '?']
del list5[0]  # 删除下标为0的元素
print(list5)  # ['are', 'you', 'doing', '?']

#del list5[20] 报错 下标越界

del list5[-1]  # 可以使用负数下标
print(list5)  # ['are', 'you', 'doing']

del list5[0:2]  # 使用切片的方式 可以删除某段元素
print(list5)  # ['doing']

# 使用方法pop()删除末尾元素 会返回删除元素的值 参数不传默认删除尾部元素  或者 传入需要删除元素指定索引下标
list6 = ["never", "give", "up"]
print(list6)  # ['never', 'give', 'up']
pop_value = list6.pop()  # 将list4尾部元素删除并返回被删除元素的值，赋值给变量pop_value
print(pop_value)  # up
print(list6)  # ['never', 'give']

list6.pop(-1)  # 可以传入负数下标
print(list6)  # ['never']

#list6.pop(5)  # 报错 下标越界 下标不能超过最大索引下标

# 使用remove()方法根据元素值来删除
list7 = ["a", "b", "c", "d", "c"]
print(list7)  # ['a', 'b', 'c', 'd', 'c']

list7.remove("a")  # 删除元素值为 "a"的元素
print(list7)  # ['b', 'c', 'd', 'c']

list7.remove("c")  # 删除元素值为 "c"的元素 只删除一个，并不会删除全部
print(list7)  # ['b', 'd', 'c']

#list7.remove("a") 传入一个列表内不存在的值 会报错 ValueError: list.remove(x): x not in list


# 3.列表的运算
# []+[]=[] 列表相加 会对两个列表进行合并
print(["hello", "python"] + ["c#", "c++"])  # ['hello', 'python', 'c#', 'c++']

# []*正整型=[] 列表会将列表内的元素重复整数倍
print(["hello", "boy"] * 3)  # ['hello', 'boy', 'hello', 'boy', 'hello', 'boy']

