import re

# group()分组
str = "Life is like the ocean and is beautiful"

mat = re.search("Life(.*)ocean and(.*)",str)

# group()默认值为0 为完整的匹配结果
print(mat.group())  # Life is like the ocean and is beautiful
print(mat.group(0))  # Life is like the ocean and is beautiful

# group(1)为内部的第1个分组匹配的内容
print(mat.group(1))  #  is like the

# group(2)为内部的第2个分组匹配的内容
print(mat.group(2))  #  is beautiful

