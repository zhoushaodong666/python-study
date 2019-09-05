# 导入一个包的模块 也会自动执行那个包的__init__.py文件 常用于初始化工作
#import package_test.module01

# 包下的__init__.py 文件中的 内置变量__all__ = ['module01'] 说明只有module01能导入 module02不在__all__内 所以无法被导入 使用会出现无定义的错误
from package_test import *
print(module01.a)  # 我是13-包和模块/package_test/module01模块的 a
#print(module02.a2)  # NameError: name 'module02' is not defined