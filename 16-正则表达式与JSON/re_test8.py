import re

# Python 的re模块提供了re.sub用于替换字符串中的匹配项。
"""
re.sub(pattern, repl, string, count=0, flags=0)
参数：

pattern : 正则中的模式字符串。
repl : 替换的字符串，也可为一个函数。
string : 要被查找替换的原始字符串。
count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
flags : 编译时用的匹配模式，数字形式。
"""


str1 = "PythonJavaC++C#GoPython"
sub1 = re.sub("Python","Rust",str1)
print(sub1)  # RustJavaC++C#GoRust

# 第4个参数count默认为0，表示替换所有的匹配，也可自己指定替换的次数
sub2 = re.sub("Python","Rust",str1,0)
print(sub2)  # RustJavaC++C#GoRust

sub3 = re.sub("Python","Rust",str1,1)
print(sub3)  # stJavaC++C#GoPython


