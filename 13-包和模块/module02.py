# 常用导入方式
# import 模块名
import module01

# 使用as别名导入 常用于较长的模块名
# import 模块名 as 别名
import package_test.module01 as pt01


print(module01.a)  # 我是13-包和模块/module01模块的 a
print(pt01.a)  # 我是13-包和模块/package_test/module01模块的 a