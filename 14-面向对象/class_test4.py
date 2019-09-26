# 继承 pyhton的类可以继承 继承来自父类的特性 然后自己可以扩展自己的特性
# 假如车是父类,那么四轮汽车,三轮车就是父类,继承父类是车的特性,然后自己还扩展了是四轮还是三轮的特性
# 格式
"""
class FatherClass():
    # 类主体



class ChildClass(FatherClass):
    # 类主体

"""


class Person():
    sum = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Person __init__ 执行")

    def printInfo(self):
        print("name:"+self.name)
        print("age:"+self.age)


class Student(Person):
    pass

#  __init__() missing 2 required positional arguments: 'name' and 'age'
# 说明Student类从父类Person继承了__init__()方法和类变量、实例变量
# s1 = Student()

s1 = Student("小白",18)
print(s1.sum)
print(s1.name)
print(s1.age)
print(Person.sum)





