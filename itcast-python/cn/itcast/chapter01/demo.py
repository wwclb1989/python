# python的一些web框架，如Django、Flask、Tornado、web2py

# python2与python3的区别：
# print()函数替代了pring语句
# python3默认使用utf8编码
# python3中的/号，整数相除结果会是浮点数
print(1 / 2)
# 使用//进行的除法，为向下取整除法
print(8 // 3)
# python3八进制字面量表示
print(0o1000)
# python3不等运算符只有一种写法!=
print(1 != 2)
# python3去除了long型，只有一种整型int，新增了bytes类型
b = b'china'
print(type(b))
# 字符串对象和bytes对象可以使用.encode()(str -> bytes)或者.decode(bytes -> str)方法相互转换
s = b.decode()
print(s)
b1 = s.encode()
print(b1)