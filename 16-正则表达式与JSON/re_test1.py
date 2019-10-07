import re
# 正则表达式
# 是一个特殊的字符序列，它能帮助你方便的检查一个字符串是否与某种模式匹配。
# 正则表达式的特殊序列指的是【普通字符】和【元字符】，正则表达式主要学习的是【元字符】
# 作用：常用于爬虫、替换字符、匹配字符
# python有个re模块，re 模块使 Python 语言拥有全部的正则表达式功能。

# re.findall()函数 返回要匹配字符串的中存在的符合既定正则的字符串的列表
"""
函数语法：

re.findall(pattern, string, flags=0)
"""
# 匹配python字符
str1 = "hello world and python、python、java、c++"
list1 = re.findall("python",str1)
print(list1)  # ['python', 'python']


# 匹配数字 使用元字符
# 我们不能再像之前使用"pyhton"这样的普通字符串去匹配，我们需要借助【元字符】
str2 = "hello12world565and0python321pytho77na65497c+"
list2 =re.findall("\d",str2)  # ['1', '2', '5', '6', '5', '0', '3', '2', '1', '7', '7', '6', '5', '4', '9', '7']
print(list2)

# 匹配非数字
str3 = "hello12world565and0python321pytho77na65497c+"
list3 = re.findall("\D",str3)
print(list3)  # ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd', 'a', 'n', 'd', 'p', 'y', 't', 'h', 'o', 'n', 'p', 'y', 't', 'h', 'o', 'n', 'a', 'c', '+']


