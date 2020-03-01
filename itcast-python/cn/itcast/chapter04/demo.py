# 跟普通的注释相比，使用三引号标注的注释会作为函数的一个默认属性，可以通过“函数名._doc_”进行访问
def len(*args, **kwargs):
    """Return the number of items in a container."""
    pass
print(len.__doc__)
# 切片[起始:结束:步长]
# 保持原始字符串，可以在字符串的前面加一个r或者R
# 字符串的格式化输出
name = "小明"
print("大家好，我叫%s"%name)
age = 20
print("大家好，我叫%s，今年%d岁了"%(name, age))
dic = {'name':'小明', 'age':29}
print("%%大家好，我叫%(name)s，今年%(age)d岁了"%dic)
# 字符串模板
from string import Template
string = Template('我叫$name, 今年$age岁。')
print(string.substitute(name = "小明", age = 28))
print(string.safe_substitute(name = "小明"))
print(string.substitute(dic))

string = Template('$$It is ${x}ful')
print(string.substitute(x = 'wonder'))

# 字符串的内建函数
# 序列类型操作相关函数len(), max(), min(), enumerate()
string = 'abcdefg'
for index, value in enumerate(string):
    print(index, value)
# 字符串类型转换相关函数chr(), ord()
print(chr(97))
print(ord('a'))
# 字符串的常见方法find, index, replace, split, lower, strip, format,
# str.find(sub[, start[, end]])
word = 'Hello, Welcome to itheima'
word.find('itheima')
word.find('itcast')
word.find('itheima', 0, 15)

# index方法如果找到了子串，则返回开始的索引值，否则会抛出ValueError异常
# str.index(sub[, start[, end]])
word = 'itheima and itcast'
word.index('it')
word.index('it', 2)

# replace(self, old, new, count=None)
# new作为新的子串会取代old旧子串，方法返回的是字符串中的old替换成new后生成的新字符串。如果给定了可选参数count,则替换不超过count次

# str.split(self, sep=None, maxsplit=-1)
word = "1 2 3 4 5"
word.split()
word = "a,b,c,d,e"
word.split(",")
word.split(",", 3)

# str.strip(chars=None)
# strip用于去除字符串两侧的空格，也可以指定字符串

# format
print('H{}'.format('ello'))
print('{0} {1}'.format('Hello', 'Python'))

# 使用比较运算符比较字符串==
# python中的成员运算符（in 和 not in），可以用来判断一个元素是否存在于某个序列中。
print('it' in 'itheima')
print('cast' not in 'itheima')
