# 1.列表:由一系列按特定顺序排列的元素组成。
# 你可以创建包含字母表中所有字母、数字0~9或所有家庭成员姓名的列表；
# 也可以将任何东西加入列表中，其中的元素之间可以没有任何关系。
# 在Python中，用方括号（ [] ）来表示列表，并用逗号来分隔其中的元素。

# example1 列表内元素都是同一种数据类型
print(type([1,2,3,4])) # <class 'list'>

# example2 列表内元素不是同一种数据类型
print(type([1,2,"hello","world"])) # <class 'list'>

# example3 列表内嵌套列表 类似其它语言的多维数组的概念
print(type([[1,2], ["hello","world"], [True,False], [1.0,2.0]])) # <class 'list'>

# 2.列表元素的访问 通过下标访问列表元素 下标从0开始 最大下标是列表长度减1
# example4
list1 = ["nice","to","meet","you"]
print(list1[0])  # nice
print(list1[3])  # you
print(len(list1))  # 4

# list1的长度是4 最大下标应该是3 我们访问4 超过了最大下标 会报错显示下标越界 IndexError: list index out of range
#print(list1[4])

# 列表也有和字符串一样的截取方式 [x:x] 截取完得到的还是一个列表
print(list1[-1:])  # ['you']

# 3.列表的运算
# []+[]=[] 列表相加 会对两个列表进行合并
print(["hello", "python"]+["c#", "c++"])  # ['hello', 'python', 'c#', 'c++']

# []*正整型=[] 列表会将列表内的元素重复整数倍
print(["hello", "boy"]*3)  # ['hello', 'boy', 'hello', 'boy', 'hello', 'boy']






