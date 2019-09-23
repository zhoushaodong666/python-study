# 成员的可见性

class Student2:
    name = ""
    age = 0
    __score = 0

    def __init__(self):
        print("__init__ 执行")

    def __method(self):
        print("__method 执行")


# 私有的成员  不给外界访问 只能在类的内部访问
# 私有用"__"（两个下划线）在变量名或者方法名前加上 eg: __name = ""  def __defName():pass

# 外界访问私有成员会报异常
s1 = Student2()
print(s1.name,s1.age)
#print(s1.__score)  # AttributeError: 'Student2' object has no attribute '__score'
#s1.__method()  # AttributeError: 'Student2' object has no attribute '__method'
