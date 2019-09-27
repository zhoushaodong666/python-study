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
    def __init__(self,id,school,name,age):
        self.id = id
        self.school = school
        # 第1种调用父类构造函数的方法：父类名.__init__()(不推荐)

        # 此时要传入self实例对象 是因为平常我们直接 【对象名.方法名()】是传入了self对象的
        # 如果使用【类名.方法名()】是没有传入self对象的，所以需要显示的传入对象名self
        #Person.__init__(self,name,age)

        # 第2种调用父类构造函数的方法: super(子类名,对象名).__init__(参数列表) (推荐)
        # python提供的super就是用来调用父类方法的
        super(Student,self).__init__(name,age)

s1 = Student("0101","清华大学","小白",22)
print(s1.__dict__)
