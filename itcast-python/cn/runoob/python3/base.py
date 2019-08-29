# python -V
print("hello world!")
import keyword

keyword.kwlist
x = "a"
y = "b"
print(x)
print(y)
print(x, end="")
print(y, end="")
#     type()不会认为子类是一种父类类型。
#     isinstance()会认为子类是一种父类类型。
a = 111
print(type(a))
print(isinstance(a, int))
b = "hello"
print(type(b))
print(isinstance(b, str))
# 列表、元组、集合、字典
list = ['abcd', 786, 2.23, 'runoob', 70.2]
print(list)
tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
print(tuple)
set = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(set)
dict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}
print(dict)

# if
if a < 10:
    print("a是一位数")
elif a < 100:
    print("a是两位数")
else:
    print("a是三位数以上")

# 循环，计算从1到100的和
sum = 0
i = 1
while i <= 100:
    sum += i;
    i += 1;
else:
    print("计算结束！i =", i)
print(sum)

sum = 0
for i in range(1, 101):
    sum += i;
print("for语句循环得到的sum=", sum)

# 迭代器
it = iter(list)
print(next(it))
print(next(it))
print("------")
for x in it:
    print(x)


# 函数
def hello():
    print("hello world!")


hello()

# 必需参数
# 关键字参数
# 默认参数
# 不定长参数


# L （Local） 局部作用域
# E （Enclosing） 闭包函数外的函数中
# G （Global） 全局作用域
# B （Built - in） 内置作用域（内置函数所在模块的范围）

import sys

print('命令行参数如下:')
for i in sys.argv:
    print(i)

print('\n\nPython 路径为：', sys.path, '\n')
