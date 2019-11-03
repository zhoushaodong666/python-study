# map(func, *iterables)
# 将第二个参数迭代器中的元素都当做参数，传给第一个参数中的函数‘

# 将传入的数字翻倍
def double_num(x):
    return 2*x

list1 = [1,2,3,4,5]
list2 = [2,4,6,8,10]
res = map(double_num,list1)
print(list(res))  # [2, 4, 6, 8, 10]

# map与lambda表达式
res2 = map(lambda x:2*x,list1)
print(list(res2))  # [2, 4, 6, 8, 10]

# map第二个参数是可变参数 可以传入多个参数
res3 = map(lambda x,y:x+2*y,list1,list2)
print(list(res3))  # [5, 10, 15, 20, 25]
