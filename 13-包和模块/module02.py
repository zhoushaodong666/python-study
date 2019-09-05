# 常用导入方式
# import 模块名
import module01

# 使用as别名导入 常用于较长的模块名
# import 模块名 as 别名
import package_test.module01 as pt01
print(pt01.a)  # 我是13-包和模块/package_test/module01模块的 a

# 使用 from xx import xx 导入模块 变量 函数
from package_test.module01 import b # 从package_test包下的module01模块中导入变量b
print(b)  # 我是13-包和模块/package_test/module01模块的 b

from package_test import module01 # 从package_test包导入module01模块
print(module01.a)  # 我是13-包和模块/module01模块的 a

from package_test.module01 import sayHello # 从package_test包下的module01模块导入sayHello函数
sayHello()  # hello

# 使用 from xx import * 如果嫌导入的东西太多，可以使用 * ，代表全部 但一般不推荐，最好按需导入
# 也可以在模块内 用 __all__ = [x,x,x] 定义全部*可导出的变量
from package_test.module01 import *
print(a)  # 是13-包和模块/package_test/module01模块的 a
print(b)  # 是13-包和模块/package_test/module01模块的 b
print(c)  # 是13-包和模块/package_test/module01模块的 c

# package_test.module01模块内的 __all__= ['a','b','c'] 并没有d 所以无法导入
#print(d)  # NameError: name 'd' is not defined






