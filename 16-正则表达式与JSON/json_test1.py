import json
# json
# 是一种轻量级的数据交换格式 常用的数据交换格式还有xml
# 优势
# 1.易于阅读
# 2.易于解析
# 3.跨语言交换数据
# 4.网络传输效率高

# 举例： {"name":"tom",age:12}
# {}代表对象
# []代表数组
# 键名必须用双引号引起来


"""
json        python

object      dict
array       list
string      str
number      int
number      float
true        True
false       False
null        None
"""

# 反序列化 即把json字符串转换成相应编程语言的数据结构 方便操作json字符串

# python则是将json对象转换成dict字典
json_str1 = '{"name":"tom","age":12}'
json_dict = json.loads(json_str1)
print(type(json_dict))  # <class 'dict'>
print(json_dict)  # {'name': 'tom', 'age': 12}
print(json_dict['name'])  # tom
print(json_dict['age'])   # 12

# python则是将json数组转换成list列表 内部的对象则转换成dict字典
json_str2 = '[{"name":"tom","age":12},{"name":"Bob","age":18}]'
json_list = json.loads(json_str2)
print(type(json_list))  # <class 'list'>
print(json_list)  # [{'name': 'tom', 'age': 12}, {'name': 'Bob', 'age': 18}]
print(json_list[0])  # {'name': 'tom', 'age': 12}
print(json_list[1])  # {'name': 'Bob', 'age': 18}
print(type(json_list[0]))  # <class 'dict'>

# 序列化 即将相应编程语言的数据结构转换成json字符串

json_list2  = [{"name":"Smith","age":18,"married":False},{"name":"COCO","age":20,"married":True}]
json_str3 = json.dumps(json_list2)
print(json_str3)  # [{"name": "Smith", "age": 18, "married": false}, {"name": "COCO", "age": 20, "married": true}]
