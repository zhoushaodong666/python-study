# str 字符串 可以用 单引号 双引号 三引号表示
str1 = "我是双引号字符串"
print(str1)

str2 = '我是单引号字符串'
print(str2)

# 多行字符串可以直接换行
str3 = """我是多行字符串
啦啦啦啦"""
print(str3)

# 如果单引号和双引号的字符串想换行呢？
# 单双引号换行需要在末尾加上\
str4 = "我要\
换行"
print(str4)

str5 = '我要\
换行'
print(str5)

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


# 转义字符
# 1.无法用肉眼直接看出的字符
# example 1
print("我是\nexample 1") #该结果会换行输出 换行符就不是我们肉眼能直接看到的字符

# 2.常见的转移字符
# \n换行 \r回车 \t横向制表符

# 3.如果想原样输出example1的\n，怎么做呢?
# 我们可以使用 \\n原样输出\n的字符
print("我是\\nexample 1")

# 4.如果转义字符很多，难道我们都要加\吗?
# 我们可以使用原生字符串 就是我们传入什么输出的就是什么 像\n这种转义字符不会给识别出来,就当成普通字符
print(r"\ndsfsdaf\nsdfdsaf\t") # \ndsfsdaf\nsdfdsaf\t
print(R"\ndsfsdaf\nsdfdsaf\t") # \ndsfsdaf\nsdfdsaf\t

#字符串的运算
# 1.拼接字符串 使用"+"
print("hello"+"world") #helloworld

# 2.字符串重复 使用"*" *后面跟整数,跟着几就重复字符串几遍
print("hello"*2) #hellohello

# 3.下标获取字符串中的单个字符
# 从下面的三个我们可以得到一个规律 我们的下标是从0开始的 和其他语言的数组从下标0开始一样 不同的是我们可以传入负整数
# 规律：下标从0开始 -0也是0 所以还是取的第一个字符 -1代表从最后一个字符数1个取到的字符，-号代表反向
print("hello world"[0]) # h
print("hello world"[-0]) # h
print("hello world"[-1]) # o

# 4.下标获取字符串中的一截字符串
# 从下面的两个 我们可以得到结论是 字符串用[x:x]的形式取一截字符串 第二个是下标的元素是不被包含进来的 所以我们要多取一个

# 我们来获取下 hello这一截字符串
print("hello world"[0:4]) # hell
print("hello world"[0:5]) # hello

# 5.如果截取某个下标后面的全部字符串
# 我们截取"hello "后面的全部字符串 [x:]
print("hello c# python java rust"[6:]) # c# python java rust
# 同理 假如想截取rust前面的全部字符串
print("hello c# python java rust"[:-4]) # hello c# python java

