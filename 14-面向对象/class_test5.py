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
        Person.__init__(self,name,age)

s1 = Student("0101","清华大学","小白",22)
print(s1.__dict__)
