import re
# 正则表达式
# 是一个特殊的字符序列，它能帮助你方便的检查一个字符串是否与某种模式匹配。
# python有个re模块，re 模块使 Python 语言拥有全部的正则表达式功能。
# 这里主要介绍re模块的函数的使用，正则表达式不了解的，可以另外查找资料。

# 1. re.match函数
# 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
"""
函数语法：

re.match(pattern, string, flags=0)
"""
print(re.match("www","www.baidu.com").span())
