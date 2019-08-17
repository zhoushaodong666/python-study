# 字典
# 是一系列键 — 值对 。每个键都与一个值相关联，你可以使用键来访问与之相关联的值。与键相关联的值可以是数字、字符串、列表乃至字典
# 字典的定义

dict1 = {'a': 1, 'b': '3'}
print(dict1)  # {'a': 1, 'b': '3'}
print(type(dict1))  # <class 'dict'>

# 字典的访问
dict2={"name": "tom", "age": 12}
print(dict2)  # 'name': 'tom', 'age': 12}
print(dict2["name"])  # tom
print(dict2["age"])  # 12

# 访问字典中不存在的键 会抛出错误

#print(dict2["aa"]) KeyError: 'aa'

# 字典中键值的修改
dict3 = {"name": "david", "age": 18}
print(dict3)  # {'name': 'david', 'age': 18}
dict3["name"] = "atom"  # 修改dict3中键名为name的值为atom
dict3["age"] = 20  # # 修改dict3中键名为age的值为20
print(dict3)  # {'name': 'atom', 'age': 20}

# 字典的删除 使用del关键字可以删除某个键值对 也可以删除整个字典
# 删除某个键值对
dict4 = {"name": "bob", "age": 18}
print(dict4)  # {'name': 'bob', 'age': 18}
del dict4["name"] #删除dict4中键名为name的键值对
print(dict4)  # {'age': 18}

# 删除整个字典
del dict4
#print(dict4)  # 抛出一个异常 NameError: name 'dict4' is not defined



