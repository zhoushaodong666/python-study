import re

# 字符集 中括号"[]"
# [amd] 匹配字符'a'或'm'或'd'

# 匹配中间字符是'b'、'c'、'd',第一个字符是'a',第三个字符是'd'的全部字符串
str1 = "abd,abc,add,aef,aed,acc,aee,aff,aed,acd"
list1 = re.findall("a[bcd]d",str1)
print(list1)  # ['abd', 'add', 'acd']

# bcd是连续的 我们可以使用"-",b-d表示b到d的全部字母，即bcd
list2 = re.findall("a[b-d]d",str1)
print(list2)  # ['abd', 'add', 'acd']


