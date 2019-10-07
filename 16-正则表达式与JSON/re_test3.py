import re

# 元字符
# \d 匹配一个数字字符。等价于 [0-9]。
str1 = "java321python123c++/__"
list1 = re.findall("\d", str1)
print(list1)  # ['3', '2', '1', '1', '2', '3']

list2 = re.findall("[0-9]", str1)
print(list2)  # ['3', '2', '1', '1', '2', '3']

# \D 匹配一个非数字字符。等价于 [^0-9]。 ^用在[]内是取反的作用
list3 = re.findall("\D", str1)
print(list3)  # ['j', 'a', 'v', 'a', 'p', 'y', 't', 'h', 'o', 'n', 'c', '+', '+', '/', '_', '_']

list4 = re.findall("[^0-9]", str1)
print(list4)  # ['j', 'a', 'v', 'a', 'p', 'y', 't', 'h', 'o', 'n', 'c', '+', '+', '/', '_', '_']

# \w 匹配字母、数字、下划线。等价于'[A-Za-z0-9_]'。
list5 = re.findall("\w", str1)
print(list5)  # ['j', 'a', 'v', 'a', '3', '2', '1', 'p', 'y', 't', 'h', 'o', 'n', '1', '2', '3', 'c', '_', '_']

list6 = re.findall("[A-Za-z0-9_]", str1)
print(list6)  # ['j', 'a', 'v', 'a', '3', '2', '1', 'p', 'y', 't', 'h', 'o', 'n', '1', '2', '3', 'c', '_', '_']

# \W 匹配非字母、数字、下划线。等价于 '[^A-Za-z0-9_]'。
list7 = re.findall("\W", str1)
print(list7)  # ['+', '+', '/']

list8 = re.findall("[^A-Za-z0-9_]", str1)
print(list8)  # ['+', '+', '/']

str2 = "sdaf\f asdf\ndsf \r32\t__\v"

# \s 匹配任何空白字符，包括空格、制表符、换页符等等。等价于 [ \f\n\r\t\v]。

# \f 匹配一个换页符。等价于 \x0c 和 \cL。
# \n 匹配一个换行符。等价于 \x0a 和 \cJ。
# \r 匹配一个回车符。等价于 \x0d 和 \cM。
# \t 匹配一个制表符。等价于 \x09 和 \cI。
# \v 匹配一个垂直制表符。等价于 \x0b 和 \cK。

list9 = re.findall("\s", str2)
print(list9)  # ['\x0c', ' ', '\n', ' ', '\r', '\t', '\x0b']

list10 = re.findall("[ \f\n\r\t\v]", str2)
print(list10)  # ['\x0c', ' ', '\n', ' ', '\r', '\t', '\x0b']

# \S	匹配任何非空白字符。等价于 [^ \f\n\r\t\v]。
list11 = re.findall("\S", str2)
print(list11)  # ['s', 'd', 'a', 'f', 'a', 's', 'd', 'f', 'd', 's', 'f', '3', '2', '_', '_']

list12 = re.findall("[^ \f\n\r\t\v]", str2)
print(list12)  # ['s', 'd', 'a', 'f', 'a', 's', 'd', 'f', 'd', 's', 'f', '3', '2', '_', '_']
