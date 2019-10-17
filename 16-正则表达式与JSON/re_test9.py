import re

# re.match()和re.search()的使用
"""
语法：
re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
re.match(pattern, string, flags=0)

re.search 扫描整个字符串并返回第一个成功的匹配。
re.search(pattern, string, flags=0)
flag：
    re.I	使匹配对大小写不敏感
    re.L	做本地化识别（locale-aware）匹配
    re.M	多行匹配，影响 ^ 和 $
    re.S	使 . 匹配包括换行在内的所有字符
    re.U	根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
    re.X	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。
"""

str1 = "A16ASD8F6AD5S1F"
str2 = "16ASD8F6AD5S1F"

# 匹配数字

# re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
res1 = re.match("\d",str1)
res2 = re.match("\d",str2)
print(res1)  # None
print(res2)  # <re.Match object; span=(0, 1), match='1'>

# re.search 扫描整个字符串并返回第一个成功的匹配。
res3 = re.search("\d",str2)
print(res3)  # <re.Match object; span=(0, 1), match='1'>
