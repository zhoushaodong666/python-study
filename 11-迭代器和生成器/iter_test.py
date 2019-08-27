import sys

# 迭代器是一个可以记住遍历的位置的对象。
# 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
# 迭代器有两个基本的方法：iter() 和 next()。
list1 = [1, 2, 3, 4]
it1 = iter(list1)
print(next(it1))  # 1
print(next(it1))  # 2

# 使用for语句对迭代器对象进行遍历
list2 = [1, 2, 3, 4]
it2 = iter(list2)
for x in it2:
    print(x, end=" ")
# 输出结果
# 1 2 3 4

# 	使用next()函数
list3 = [1, 2, 3, 4]
it3 = iter(list3)
while True:
    try:
        print(next(it3), end="\n")
    except StopIteration:
        sys.exit()

# 输出结果
# 1
# 2
# 3
# 4



