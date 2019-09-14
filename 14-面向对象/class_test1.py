# 1.类的定义
# 类是具有相同特征的一类事物,描述具有相同的属性和方法的对象的集合

# 格式：
"""
class ClassName():
    类体
"""

# 写一个简单的类
class Student():
    # 类的属性
    age = 0
    name = ''

    # 构造方法
    def __init__(self):
        print("我是构造方法")

    # 类的方法
    def printHello(self):
        print("hello")

    def printTest(self):
        print(self)
        print(self.__class__)

# 2.类的对象
# 类是抽象的,实例对象是具体。 就好像手机设计图一样是抽象的,拿到手里的苹果手机是具体的。
# 格式：
"""
x = ClassName()
"""

# 实例化一个Student类的对象
s = Student()

# 3.类的方法
# 类中定义的函数称为方法
# 类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self
# 格式：
"""
def methodName(self):
    pass
"""
# 【self】输出类的实例对象的当前内存地址
# 【self.class】 指向类
s.printTest()
# 输出结果
# <__main__.Student object at 0x0000029312E58188>
# <class '__main__.Student'>










