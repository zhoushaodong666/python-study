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
# 类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是【self】,也可以是其他名称.
# self指向调用类的方法的实例对象
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
    # 类的属性/类的变量
    des = "这是一个Person类"
    name = 'jason'

    def __init__(self, name, age):
        # 使用self.xx的方式 将形参的值保存到实例对象的实例变量中
        self.name = name
        self.age = age
        self.test = "test"
        print("我是__init__方法")
        print("name:" + name)
        print("age:" + str(age))
        # return "person"

    def printPerson(self):
        self.ha = "df"
        pass
        # print("类变量name:"+name)

    def printObjectMethod(self):
        print("实例方法")

    # 类方法
    @classmethod
    def classMethodName(cls):
        print("classMethodName 类的方法执行")
        print("类的属性 des:", cls.des)

    @staticmethod
    def staticMethodName():
        print("staticMethodName 静态方法执行")



# 实例化类对象 会自动调用一次__init__()方法
p = Person("小丽", 16)
# 我是__init__方法
# name:小丽
# age:16

print("=====================")

# 4.类变量，定义在类中且在方法之外，Person类的变量des就是类变量,通过【类名.变量名】来访问变量
print(Person.des)  # 这是一个Person类
Person.des2 = "这是一个Person类2"
print(Person.des2)  # 这是一个Person类2

print("=====================")

# 5.实例变量，定义在方法内部，变量是保存在实例对象中的，通过【self(实例).变量名】来访问实例变量
p2 = Person("小白", 18)
p3 = Person("小红", 20)

print(p2.name)  # 小白
print(p2.age)  # 18

print(p3.name)  # 小红
print(p3.age)  # 20

# 内置变量__dict__可以查看pyhton类实例的全部实例变量
print("p2的全部实例变量", p2.__dict__)  # p2的全部实例变量 {'name': '小白', 'age': 18, 'test': 'test'}
print("p3的全部实例变量", p3.__dict__)  # p3的全部实例变量 {'name': '小红', 'age': 20, 'test': 'test'}

print("=====================")

# 6.类变量和实例变量的访问顺序

# 使用实例对象访问变量 优先从实例变量中找 没有再向上找类变量
print(p3.des)  # 这是一个Person类
print(p3.name)  # 小红
print(Student.age)  # 0
print(Student.name)  # ''
print("=====================")

# 7.构造方法也可以自己显式的调用
p.__init__("小白", 18)
# 我是__init__方法
# name:小白
# age:18

# 构造方法的返回值只能是None,不能是其他的。None一般不写,函数会自动返回。
# print(p)  # TypeError: __init__() should return None, not 'str'

# 8.类的方法 使用classmethod的修饰符定义,classmethod修饰符对应的函数不需要实例化，不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等
# 格式：
"""
@classmethod
def classMethodName(cls):
    pass
"""

#  类名调用类的方法
Person.classMethodName()
# classMethodName 类的方法执行
# 类的属性 des: 这是一个Person类

# 实例对象调用类的方法
p.classMethodName()
# classMethodName 类的方法执行
# 类的属性 des: 这是一个Person类


# 9.静态方法
# 使用@staiticmethod来修饰一个方法，该方法不强制传递参数
# 格式：
"""
@staticmethod
    def staticMethodName():
        pass
"""
print("=============")
# 使用类名调用静态方法
Person.staticMethodName()  # staticMethodName 静态方法执行

# 使用实例对象调用静态方法
p.staticMethodName()  # staticMethodName 静态方法执行