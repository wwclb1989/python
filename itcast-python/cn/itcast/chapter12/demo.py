# 第12章 错误和异常
# 常见的内建异常：Exception, SyntaxError, FileNotFoundError, NameError,
# ZeroDivisionError, IndexError, KeyError, AttributeError, TypeError

# try-except-else-finally语句格式：
# try:
#     可能出错的代码
# except [错误类型] as error:
#     出错后的处理语句
# else:
#     未出错时执行的语句
# finally:
#     无论是否出错都执行的语句

# 抛出异常：raise 异常类名，raise 异常类实例对象，raise
# 异常中抛出另一个异常，raise...from...
# try:
#     num
# except Exception as exception:
#     raise IndexError("下标超出范围") from exception

# assert断言语句用于判定一个表达式是否为真

# with语句处理异常
try:
    file = open('/test.txt')
    try:
        for aline in file:
            print(aline)
    except Exception as error:
        print(error)
    finally:
        file.close()
except FileNotFoundError as err:
    print(err)

try:
    with open('/test.txt') as file:
        for aline in file:
            print(aline)
except Exception as error:
    print(error)