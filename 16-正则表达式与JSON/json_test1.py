import json
# json
# 是一种轻量级的数据交换格式 常用的数据交换格式还有xml
# 优势
# 1.易于阅读
# 2.易于解析
# 3.跨语言交换数据
# 4.网络传输效率高

# 举例： {"name":"tom",age:12}
json_str = "{'name':'tom','age':12}"

json = json.loads(json_str)
print(json)