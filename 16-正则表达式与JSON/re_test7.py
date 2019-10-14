import re

# 匹配模式
# re.findall(pattern, string, flags=0) 第3个参数flag的使用
# 常用的有 I(忽略英文字母的大小写) S(使"."可以匹配任意字符)
str = "Javajava\npythonjava1"
list1 = re.findall("java",str)
print(list1)  # ['java', 'java']

list2 = re.findall("java",str,re.I)
print(list2)  # ['Java', 'java', 'java']

list3 = re.findall("java.{1}",str)
print(list3)  # ['java1']

list4 = re.findall("java.{1}",str,re.S)
print(list4)  # ['java\n', 'java1']