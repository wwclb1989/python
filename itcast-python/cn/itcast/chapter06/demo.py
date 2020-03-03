# 第6章 流程控制
# if, while, for
# 在python中，所有的值都可以当作bool值，这点与js一样
# 可以使用bool()函数判断一个表达式的值
# and, or, not
# 判断表达式，类似java的三目运算符：表达式 if 值1 else 值2

# while 表达式:
#     执行语句

# for 临时变量 in 可迭代对象:
#     执行语句
# 在循环遍历序列时，索引位置和对应值可以使用enumerate()函数同时得到
for i, v in enumerate(["I", "love", "Itcast"]):
    print(i, v)
# 在同时循环遍历两个或多个序列时，可以使用zip()函数将这些序列打包
infos = ["姓名", "年龄", "性别"]
student = ["小明", "22", "男"]
for (i, s) in zip(infos, student):
    print('学生的{}是{}'.format(i, s))
# reversed函数，逆向循环
for i in reversed(range(1, 5)):
    print(i)
# sorted函数，排序循环
colors = ['red', 'green', 'yellow', 'white', 'black']
for c in sorted(colors):
    print(c)
# 使用iter()函数得到一个可迭代序列的迭代器对象
# 列表推导式是利用现在列表创建一个新列表的方法
# [新元素表达式 for 临时变量 in 可迭代对象 if 条件表达式]
# 列表推导式可以叠加多个for循环
demo_list = [(x, y) for x in range(2) for y in range(3)]
print(demo_list)
# break与continue作用与java相同
# pass语句表示不做任何事情
# else语句作为循环的子句，可以使循环结束后执行，但是在碰到break语句终止情况下不执行