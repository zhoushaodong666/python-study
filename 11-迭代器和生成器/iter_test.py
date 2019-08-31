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

# 生成器
# 生成器是一个返回迭代器的函数，只能用于迭代操作

def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()
# 输出结果
# 0 1 1 2 3 5 8 13 21 34 55



