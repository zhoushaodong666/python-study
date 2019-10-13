import re

# 组
# 使用"()"将指定匹配的序列分为一组
str = "PythonPythonPythonPythonPythonJavaJavaJavaJava"

# 匹配是否有5个连续Python的字符串
list = re.findall("(Python){5}",str)
print(list)  # ['Python']

# 匹配是否有6个连续Python的字符串
list2 = re.findall("(Python){6}",str)
print(list2)  # []