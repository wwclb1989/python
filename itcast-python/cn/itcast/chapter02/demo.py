# 第2章 python快速入门
# 程序的输入和输出
# print(*objects, sep = ' ', end = '\n', file = sys.stdout, flush = False)
# sep：在值之间插入字符串，默认是一个空格
# end：追加在后面值的字符串， 默认是一个换行符
# file：类似文件（流）的对象，默认是sys.stdout
# flush：是否强制刷新文件（流），默认是False
# 格式化输出
s = 'hello'
n = len(s)
print('The length of %s is %d'%(s, n))
# 程序的输入
name = input()
print("name:", name)
"""
文档字符串注释
"""
# python不支持C语言中的自增1（++）和自减1（--）运算符

# python支持三种数字类型，分别是int, float, complex
# 布尔类型是特殊的整型，它的值只有两个，分别是True和False。如果将布尔值进行数值运算，True会被当作整型1，False会被当作整型0。
# 以下对象的布尔值都是False
# None, False, 0, 0.0, 0.0 + 0.0j, "", [], (), {}, 用户自定义的类实例中实现的_bool_或者_len_()方法
# 除了上述对象之外的所有其他对象的布尔值都为True
# 字符串、元组、列表、字典、集合
# 集合的主要作用：
# （1）去重。把一个列表变成集合，会自动去重。
# （2）关系测试。测试两组数据之间是否存在交集、差集、并集等关系
# 如果要创建空的集合，必须使用set()，而不是表示空值的{}。{}用于创建空字典
student = {'Tom', "Jim", "Mary", "Tom", "Jack", "Rose"}
print(student)
# if、elseif、else、while、for * in *、iter()
# 文件读写、错误和异常、函数、类和对象、模块