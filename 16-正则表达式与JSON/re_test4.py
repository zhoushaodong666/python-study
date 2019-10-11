import re

# 数量词
# a{m,n} 将a字符重复m-n次

# 将java go rust等单词提取出来
str1 = "java324654go54.rust532swift"

# 如果使用之前方式，我们是无法提取单词的，只能提取单个字符
list1 = re.findall("[a-z]",str1)
print(list1)  # ['j', 'a', 'v', 'a', 'g', 'o', 'r', 'u', 's', 't', 's', 'w', 'i', 'f', 't']

# 使用数量词可以解决这个问题
# 提取2个字符的字符串
list2 = re.findall("[a-z]{2}",str1)
print(list2)  # ['ja', 'va', 'go', 'ru', 'st', 'sw', 'if']

# 一般单词都是2个字符以上
# 可以使用{2,} 表示2个及以上
list3 = re.findall("[a-z]{2,}",str1)
print(list3)  # ['java', 'go', 'rust', 'swift']

# 如果只匹配长度为2-5个字符的字符串
# 可以使用{2,4} 表示2个到5个
list4 = re.findall("[a-z]{2,5}",str1)
print(list4)  # ['java', 'go', 'rust', 'swift']

# 贪婪模式
# 前面的{2，}和{2,5} 为什么是匹配更多字符，而不是2个字符就停止，是因为python匹配是贪婪的，所以会尽可能的匹配更多的字符

# 非贪婪模式
# 在匹配的字符集后面加上?
list5 = re.findall("[a-z]{2,5}?",str1)

# 非贪婪模式 所以没次都匹配最少的2个字符
print(list5)  # ['ja', 'va', 'go', 'ru', 'st', 'sw', 'if']

# "*" 匹配0次或多次
# "+" 匹配1次或多次
# "?" 匹配0次或1次

str2 = "pytho1python2pythonn"
# 正则表达式"python*" "*"限制了前面的字符"n" 可以有0个或多个 所以 pytho、python、pythonn都符合
list6 = re.findall("python*",str2)
print(list6)  # ['pytho', 'python', 'pythonn']

# 正则表达式"python+" "+"限制了前面的字符"n" 可以有1个或多个 所以 python、pythonn都符合
list7 = re.findall("python+",str2)
print(list7)  # ['python', 'pythonn']

# 正则表达式"python?" "?"限制了前面的字符"n" 可以有0个或1个 所以 pytho、python、python都符合，第三个单词python来自pythonn前6个字符，因为python已经符合重复1次
list8 = re.findall("python?",str2)
print(list8)  # ['pytho', 'python', 'python']

