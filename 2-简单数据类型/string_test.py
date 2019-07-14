# str 字符串 可以用 单引号 双引号 三引号表示
str1 = "我是双引号字符串"

str2 = '我是单引号字符串'

str3 = """
我是多行字符串
"""
print(str1)
print(str2)
print(str3)

# python中为什么要有单双三引号这么多种字符串表示方法呢？

# 举例 输出 don't worry
#str4 = 'don't worry' 这么定义会报错
#print(str4)

# 正确输出 don't worry #双引号内包含单引号就不会报错了
str5 = "don't worry"
print(str5)

# 如果一定要用单引号表示呢？
# 我们需要借助 \来转义 就是告诉编译器 \后字符没有其他的意思 就是一个普通字符
str6 = 'don\'t worry'
print(str6)
