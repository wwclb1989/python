# 第7章 字典和集合
# 两个没有顺序的内建数据类型，字典为键和值的一对一映射，集合则为一个无序不重复的元素的集
# 字典是可变集合，1.同一个键被多次赋值，会被覆盖，2.字典的键必须是不可变类型，如列表就不可以当作字典的键
# 字典的创建
# dict(**kwarg)
# dict(mapping, **kwarg)
# dict(iterable, **kwarg)
print({})
print(dict([('jay',123), ('json', 1234), ('jane', 12345)]))
print(dict(sape=4139, guido=4127, jack=4098))
# 通过字典推导式创建
print({x : x ** 2 for x in (2, 4, 6)})
# 字典的访问，如果键是不存在的，会抛出KeyError异常
# 为了避免引起上述异常，访问字典元素的时候，先用in, not in来判断一个键是否存在于字典中
# 遍历字典中的元素for key in dict
# 用del可以删除字典中的元素，也可以删除整个字典，如果要删除的键不存在，会抛出KeyError异常
# hash()函数用于返回对象的哈希值

# 字典的内建方法
# copy()会返回字典的一个浅复制，即调用copy()方法会复制出一个新的字典对象，但是这个新字典引用的还是原字典对象的
# 可以通过from copy import deepcopy，使用deepcopy()函数获得字典的一个深复制副本
# 通过字典的键访问值时，如果不存在，会出现KeyError错误，为了避免，可使用get()方法
# dict.get(key[, default])
# items()返回字典的元素视图，keys()返回字典的键视图，values()返回字典的值视图


# python集合是一个存储不重复可哈希对象的无序集，可以使用set()函数创建
set_01= set([1, 1, 5, 5, 8, 8])
# 集合支持联合、相交、差补、和对称差分的数学运算
# 集合是无序的，所以不支持索引、切片或者其它类似于序列的操作
# 集合有两种内置的集合类型：set和frozenset，可变和不可变集合
set_02 = frozenset([1, 2, 3, 4, 5])
print(type(set_01))
print(type(set_02))
set_03 = {1, 2, 3, 4, 5}
print(type(set_03))
# 使用add()方法向集合中添加元素
# 使用remove()方法，删除集合中的元素，不存在时抛出KeyError异常
# 使用discard()方法，删除集合中的元素，不存在时不做任何操作
# pop()方法用于删除任意一个元素
# clear()方法删除集合的所有元素
# 另外，可以用例-=号删除集合与另一个集合的共有元素
# 集合可以用比较运算符进行比较，表示的是集合之间的子集，超集关系
# 集合运算
# 1. 联合“|”，即两个集合的并集，也可以使用union()函数
# 2. 交集“&”，即两个集合的交集，也可以使用intersection()函数
# 3. 差补“-”，即两个集合的差集，也可以使用difference()函数
# 4. 对称差分“^”，即两个集合的并集与两个集合的交集的差集，可以使用symmetric_difference()函数
# 如果参与运算的两个集合一个是可变的，一个是不可变的，结果与运算符左侧类型相同
# 可变集合类型的操作符
# 1. 联合更新“|=”，与update()方法等价
# 2. 交集更新“&=”，与intersection_update()等价
# 3. 差补更新“-=”，与difference_update()等价
# 4. 对称差分更新“^=”，与symmetric_difference_update()等价
