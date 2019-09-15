class Student():
    # 类的属性
    age = 0
    name = ''

    # 类的方法
    def printHello(self):
        print("hello")

    def printTest(self):
        print(self)
        print(self.__class__)


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
s = Student()
s.printTest()


# 输出结果
# <__main__.Student object at 0x0000029312E58188>
# <class '__main__.Student'>

# 构造方法
# 类有一个名为 __init__() 的特殊方法（构造方法），该方法在类实例化时会自动调用
# 常用与类的初始化操作

# 每次实例化类对象都会调用__init__()方法

class Person:
    # 类的属性
    name = ""
    age = 0

    def __init__(self, name, age):
        # 初始化类的属性

        # 错误写法 无法改变类的属性
        #name = name
        #age = age

        # 正确写法 使用self.xx的方式访问对象的属性
        self.name = name
        self.age = age
        print("我是__init__方法")
        print("name:" + name)
        print("age:" + str(age))
        # return "person"


# 实例化类对象 会自动调用一次__init__()方法
p = Person("小丽", 16)
# 我是__init__方法
# name:小丽
# age:16
print(p.name)
print(p.age)

print("=====================")

# 构造方法也可以自己显式的调用
p.__init__("小白", 18)
# 我是__init__方法
# name:小白
# age:18

# 构造方法的返回值只能是None,不能是其他的。None一般不写,函数会自动返回。
# print(p)  # TypeError: __init__() should return None, not 'str'
