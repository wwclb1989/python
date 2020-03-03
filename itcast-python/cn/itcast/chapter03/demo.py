# 第3章 数值类型
# type()函数可查看对象的类型
a = 0b01111
print(type(a))
b = 0o71
print(type(b))
c = 0x3A
print(type(c))
# 进制转换bin(),oct(),hex(),int()
# 整型存储方式：原码、反码、补码
# 按位取反~，按位左移<<, 按位右移>>, 按位与&，按位或|， 按位异或^
print(~9, 9 << 4)
# 浮点数与复数

# python中分别使用or, and, not作为逻辑运算或，与，非的运算符
# python3中，使用input()函数获取到的数据是一个字符串
# 类型转换函数：int(), float(), complex(), str()
# python中将对象的内存地址称为身份（id）
# 任何对象的身份都可使用内建函数id()获取
# python中的身份运算符为：is和is not