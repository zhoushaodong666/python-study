# 成员的可见性

class Student2:
    name = ""
    age = 0


    def __init__(self):
        self.__score = 60
        print("__init__ 执行")

    def __method(self):
        print("__method 执行")


    def print_test(self):
        print("print_test 执行")
        self.__method()


# 私有的成员  不给外界访问 只能在类的内部访问
# 私有用"__"（两个下划线）在变量名或者方法名前加上 eg: __name = ""  def __defName():pass
# 私有的成员名字会进行重整 Student2类中的__score会重整为_Student2__score,修改成员名字,再用之前__score访问，会报错说该属性不存在。

# 外界访问私有成员会报异常
s1 = Student2()
s2 = Student2()

# 这里为什么可以访问__score这个私有成员？
s1.__score = -1
print(s1.__score)  # -1

# 原因是实例对象的【s1.__score = -1】，是新添加一个实例变量，并不是我们在__init__()中的self.__score = 60
# 使用__dict__查看下所有变量
# 从下边的输出结果可以看出，我们在__init__中设置的【__score】被python改成了【_Student2__score】

# 重整后的名字可以访问
print(s1.__dict__)  # {'_Student2__score': 60, '__score': -1}
print(s1._Student2__score) # 60
print(s2.__dict__)  # {'_Student2__score': 60}
print(s2._Student2__score) # 60
print("===========")

# 实例方法调用私有方法
s1.print_test()
# print_test 执行
# __method 执行


# 公有的成员 即方法和变量不需要加任何修饰符
# 其他模块 实例对象 类都能调用
print(Student2.name)
