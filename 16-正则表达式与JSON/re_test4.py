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
print(list5)
