# 数字类型：布尔类型
# 假用"True"表示
bool_true = True  # 注意 不能用 true表示 不然编译器会报错
print(type(bool_true))  # <class 'bool'>
print(bool_true)  # True
print(int(bool_true))  # 1 True是int类型数据1 所以说布尔类型是数字类型的一种
print(bool(1))  # True 非零数字转布尔类型都是True
print(bool("asd"))  # True 非空值也为True

# 假用"Flase"表示
bool_false = False  # 注意 不能用 false表示 不然编译器会报错
print(type(bool_false))  # <class 'bool'>
print(bool_false)  # False
print(int(bool_false))  # 0 False是int类型数据0 所以说布尔类型是数字类型的一种
print(bool(0))  # False 0转布尔类型是False
print(bool(""))  # False 空值为False
