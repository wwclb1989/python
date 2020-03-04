# 第8章 函数和函数式编程
# 使用help命令查看相关函数的使用方法
# 值传递与引用传递：字符串、数字、元组为值传递，列表、字典为引用传递
# 列表作为参数时，如果不想被修改，可以用切片来传入
# 函数可以返回多个值，以元组形式返回

# 函数的参数传递
# 1. 位置参数传递，传入的参数，与声明的参数位置相同，数量相同
# 2. 关键字参数传递，以参数名=参数值的形式传递
# 关键字参数可以和位置参数混合使用，但是位置参数必须要出现在关键字参数之前
def test(a, b, c):
    return a, b, c
print(test(1, c = 2, b = 3))
# 在定义函数的时候，可以指定默认值
# 可变参数：以*号开始的变量args会存放所有未命名的变量参数，为元组
def test(*args):
    print(args)
test(1, 2, 3, 'a', 'b', 'c')
# 以**开始的变量kwargs会存放命名参数，为字典
def test(**kwargs):
    print(kwargs)
test(a = 1, b = 2, c = 3, d = 4)
# 如果加了*和**的参数混合使用，那么传入的顺序必须和声明时的顺序一致
# 使用*可以将未命名的参数打包成元组，使用**可以将未命名的参数打包成字典
# 解包裹与打包正好相反，在调用时对传入的元组、字典进行解包
# 混合传递方式基本原则：
# 1. 先位置参数传递
# 2. 再关键字参数传递
# 3. 再可变参数传递
# 对于函数的定义而言：
# 1. 参数arg = <value>必须位于args之后
# 2. 参数*args必须在arg = <value>后
# 3. 参数**kwargs必须在*args后

# 在python中，函数本身也可以作为参数传入另一函数并进行调用
# lambda [arg1[, arg2, ...argn] : expression
sum = lambda a, b : a + b
print(sum(1, 2))

# 常用函数
# map函数会根据提供的函数对指定的序列做映射
func = lambda x : x + 2
result = map(func, [1, 2, 3])
print(type(result))
print(result)
print(list(result))
# filter函数会对指定序列执行过滤操作
func = lambda x : x % 2
result = filter(func, [1, 2, 3, 4, 5])
print(list(result))
# reduce函数会对参数序列中的元素进行累积
from functools import reduce
func = lambda x, y : x + y
result = reduce(func, [1, 2, 3, 4, 5])
print(result)

# 变量作用域
# 局部变量是指定义在函数内部的变量，各个函数之间互不影响
# 全局变量是指定义在函数外的变量，拥有全局作用域
# global关键字用来在函数或其他局部作用域中使用全局变量
# nonlocal关键字可以在一个嵌套的函数中修改嵌套作用域中的变量
# 使用global关键字修饰的变量之前可以不存在，而nonloacl关键字修饰的变量在嵌套作用域中必须已经存在

# 闭包
def test(number_one):
    def test_in(number_two):
        print(number_one + number_two)
    return test_in
# test_in函数就是一个闭包：
# 1. 嵌套在函数里面，test函数嵌套了test_in函数
# 2. test_in中的变量是外部函数test的参数number_one
# 3. 外部函数test的返回值是内部函数test_in的引用
print(test(100))
test(100)(100)

# 装饰器，类似于java的动态代理
def wrapper(func):
    print('正在装饰')
    def inner():
        print('正在验证权限')
        func()
    return inner

@wrapper
def test():
    print("test")
test()
# 多个装饰器可以应用在一个函数上，它们的调用顺序是自下而上的

# 通用装饰器
def func(function_name):
    def func_in(*args, **kwargs):
        return function_name(*args, **kwargs)
    return func_in


# 生成器
# yield是一个关键字，一旦函数被yield修饰，python解释器会将被修饰的函数看做是一个生成器。一个生成器中可以有多个yield。
# 当生成器遇到一个yield时，会暂停运行生成器，，返回yield后面的值。当再次调用生成器的时候，会从刚才暂停的地方继续运行
def create_number():
    a, b = 0, 1
    for i in range(5):
        yield b
        a, b = b, a + b

print(type(create_number()))    # class 'generator'
print(next(create_number()))
print(list(create_number()))
# 使用next()函数获得生成器create_number的值或者__next__方法

# 生成器支持的方法
# send()
def test():
    n = 1
    while n < 10:
        temp = yield n
        print(temp)
        n += 1
result = test()
print(next(result))
print(result.send('haha'))
print(result.send('haha'))
print(result.send('haha'))
# close()可以关闭生成器
# throw()向生成器发送异常
# 迭代器对象要求支持迭代器协议，即实现对象的__next__()和__iter__()方法。
# 其中，__next__()方法返回容器的下一个元素，在结尾时引发StopIteration异常。__iter__()方法返回迭代器对象本身
# issubclass(obj, super)查看一个对象是否是一个类的实例
# isinstance(sub, super)查看一个类是否为某一个类的子类

# Python标准库-内置函数
# 1. abx(x)计算绝对值
# 2. round(number[, ndigits])函数用于对浮点数进行四舍五入求值，可指定保留多少位小数
# 3. pow(x, y[, z]) x的y次幂，然后对z求模
# 4. divmod(a, b)参数a和b是非复数，返回的是除法结果和余数组成的元组
# 5.max(), min(), sum(iterable[, start])
# 类型转换相关函数
# 1. ord()返回unicode字符对应的整数数值
# 2. chr()返回整数数值对应的unicode字符
# 3. bool()返回表达式的布尔值
# 4. slice(start, stop, step)一个切片的构造函数
# 5. dir()可以查看对象内的所有属性和方法
# 序列操作相关函数
# 1. all(iterable)用于判断可迭代对象中的元素都返回True
# 2. any(iterable)如果有一个元素是True，结果就是True
# TODO: 类、对象、属性相关函数

