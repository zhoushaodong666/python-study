# map(func, *iterables)
# 将第二个参数迭代器中的元素都当做参数，传给第一个参数中的函数‘

# 将传入的数字翻倍
def double_num(x):
    return 2*x

list1 = [1,2,3,4,5]
res = map(double_num,list1)
print(list(res))  # [2, 4, 6, 8, 10]

# map与lambda表达式
res2 = map(lambda x:2*x,list1)
print(list(res2))  # [2, 4, 6, 8, 10]
