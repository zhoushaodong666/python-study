# 循环语句
# while循环
total = 0 # 定义一个变量 初始值为0
while total < 10:  # 循环条件是total<10 执行循环语句块内容
    total += 1  # 每次循环total增加1
    print("total:",total)  # 每次循环输出total的值

# while-else语句 类似于if-else语句
loop1 = 0
while loop1<5:
    print(loop1, "loop1 小于5:")  # 每次循环输出total的值
    loop1 += 1  # 每次循环loop1增加1

else:
    print(loop1, "不小于5")

# for循环 可以遍历任何序列的项目，如一个列表或者一个字符串。

# for循环遍历字符串中的每个字符
str1 = "hello world"
for s in str1:
    print(s)
# 输出结果
# h
# e
# l
# l
# o
#
# w
# o
# r
# l
# d

# for循环遍历列表中的每个元素
list1 = ["a", "b", "c", "d"]
for x in list1:
    print(x)
# 输出结果
# a
# b
# c
# d


# break语句 终止循环语句  用在while和for循环中。
# 终止while循环举例
loop2 = 0
while loop2 < 10:
    if loop2 == 5:
        print("loop2值为", loop2, " 等于5，触发break，终止while循环")
        break
    print("loop2值为", loop2, " 不等于5，for循环继续")
    loop2 += 1

# 输出结果
# loop2值为 0  不等于5，for循环继续
# loop2值为 1  不等于5，for循环继续
# loop2值为 2  不等于5，for循环继续
# loop2值为 3  不等于5，for循环继续
# loop2值为 4  不等于5，for循环继续
# loop2值为 5  等于5，触发break，终止while循环

# 终止for循环举例
for x in range(1, 10):  # range(1,10)返回一个 1-9的列表，不包含10 范围是左闭右开
    if x == 5:
        print("x值为", x, " 等于5，触发break，终止for循环")
        break
    print("x值为", x, " 不等于5，for循环继续")
# 输出结果
# x值为 1  不等于5，for循环继续
# x值为 2  不等于5，for循环继续
# x值为 3  不等于5，for循环继续
# x值为 4  不等于5，for循环继续
# x值为 5  等于5，触发break，终止for循环

# continue语句 跳过当前循环的剩余语句，然后继续进行下一轮循环。

# for循环举例
for x in range(1, 10):
    if x == 5:
        continue
    print("x = ", x," 不等于5 输出该语句")

# 输出结果
# x =  1  不等于5 输出该语句
# x =  2  不等于5 输出该语句
# x =  3  不等于5 输出该语句
# x =  4  不等于5 输出该语句
# x =  6  不等于5 输出该语句
# x =  7  不等于5 输出该语句
# x =  8  不等于5 输出该语句
# x =  9  不等于5 输出该语句






