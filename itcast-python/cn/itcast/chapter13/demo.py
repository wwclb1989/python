# 第13章 模块
# python中可通过import与from...import...这两种方式导入文件
# import test
# test.test()
# print(test.a)

# from test import test
# test()

# 模块搜索路径
import sys
print(sys.path)

# python模块的开头通常会定义一个__all__属性，确定了from...import *语句导入的内容
from calc import *
from calc import mult
print(add(3, 4))
print(mult(3, 4))

# python中的包
# import package.module
# 包中的__init__.py文件的功能与模块文件中的__all__属性的功能相同

# 第13章 模块完结，python初级部分完结
# TODO: python高级部分 第17章 多线程编程 第18章网络编程 第19章 数据库编程 第20章 web编程
# TODO: 测试需要 第15章 正则表达式 第16章图形用户界面编程
# TODO: 了解python内存划分 第14章 内存管理