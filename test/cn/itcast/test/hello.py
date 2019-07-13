'''
    每晚夜里自我独行，随处荡
'''

"""
Python3 中有六个标准的数据类型：
    Number（数字）
    String（字符串）
    List（列表）
    Tuple（元组）
    Set（集合）
    Dictionary（字典）

Python3 的六个标准数据类型中：
    不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
    可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。 
"""

# Python可以在同一行中使用多条语句，语句之间使用分号(;)分割
print("hello world!")
counter = 100  # 整型变量
miles = 1000.0  # 浮点型变量
name = "runoob"  # 字符串

print(counter)
print(miles)
print(name)

a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a+b