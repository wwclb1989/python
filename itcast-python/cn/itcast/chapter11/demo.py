# 第11章 面向对象（下）
# 封装、继承、多态

# 封装：把属性定义为私有，在属性名前面加“__”，提供setter与getter方法

# 继承：子类不能继承父类的私有属性和方法，也不能在子类中直接访问
# 子类通过“_类名__私有元素”可以访问父类的私有属性和私有方法，但是这种方法不建议
# isinstance(obj, type)用于检查对象是否属性类的实例
# insubclass(cls, cls)用于检查前者是否是后者的子类
# python支持多继承，同名的方法，先继承哪个就会调用哪个父类的方法
# 也可以子类中以变量名=父类名.变量名的方式指定变量是继承于哪个父类
# 子类也可以重写父类的方法，并通过super()关键字可以调用父类的方法
class Father(object):
    def __init__(self):
        print("父类的构造方法")

class Son(Father):
    def __init__(self):
        super().__init__()
        print("子类的构造方法")

son = Son()

# 多态：各种子类继承自相同父类的方法，然后用不同的子类实例化父类，可以获得不同的行为

# 运算符重载
# 1. 四则运算重载
class Calculator():

    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        self.number = self.number + other

    def __sub__(self, other):
        self.number -= other

    def __mul__(self, other):
        self.number *= other

    def __truediv__(self, other):
        self.number /= other

    # 类似java中的toString()
    def __str__(self):
        return str(self.number)

calculator = Calculator(10)
calculator + 10
print(calculator)
calculator - 5
print(calculator)
calculator * 2
print(calculator)
calculator / 3
print(calculator)

# 2. 索引和分片重载
class ClassScore(object):
    def __init__(self, numbers):
        # 传递参数为列表，列表推导式
        self.scores = numbers[:]

    def __getitem__(self, index):
        return self.scores[index]

    def __setitem__(self, index, value):
        self.scores[index] = value

mathscore = ClassScore([85, 91, 95, 98])
print(mathscore[0])
print(mathscore.scores)
mathscore[0] = 100
print(mathscore.scores)
mathscore[1:3] = [99, 98, 97]
print(mathscore.scores)

# 3. 定制对象的字符串形式
# 如果只是重载了__str__方法，只有print()和str()函数可以调用这个方法进行转换。
# 重载__repr__方法，可以保证各种操作下都能正确获得实例对象自定义的字符串形式

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 类似java中的toString
    def __str__(self):
        return "str转换：我叫%s, 今年%s岁"%(self.name, self.age)

    def __repr__(self):
        return "repr转换：我叫%s, 今年%s岁"%(self.name, self.age)

tom = Person("tom", 25)
print(tom)
print(str(tom))
print(repr(tom))

# 4. __new__, object中的内建方法，用于创建类的对象，是一个静态方法
class Test(object):
    def __init__(self):
        print("执行init方法")
        print("self对象的id是%s"%id(self))

    def __new__(cls):
        print("执行new方法")
        demo_object = object.__new__(cls)
        print("demo_object对象的id是%s"%id(demo_object))
        return demo_object

test = Test()

# 首先运行了__new__方法，然后才是__init__方法
# __new__方法用于创建对象，__init__方法在__new__方法的基础上完成一些其他初始化工作，包括设置对象的私有属性等
# __init__方法的参数self，就是__new__方法返回的实例

# 5. 单例模式
class Singleton(object):
    __instance = None
    __first_init = False

    def __new__(cls, age, name):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, age, name):
        if not self.__first_init:
            self.age = age
            self.name = name
            Singleton.__first_init = True

singleton_one = Singleton(18, "xiaoMing");
singleton_two = Singleton(9, "xiaoHong")
print(id(singleton_one))
print(id(singleton_two))
print(singleton_one.age, singleton_one.name)
print(singleton_two.age, singleton_two.name)

# 6. 工厂模式：用于根据需求创建不同的对象
class Mobile(object):
    def __init__(self):
        self.name = None
        self.price = None

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

class HuaWeiMobile(object):
    def __init__(self):
        print("生产一部HuaWei手机！")

class VivoMobile(object):
    def __init__(self):
        print("生产一部Vivo手机")

class MobileFactory:
    def get_mobile(self, name):
        if name == "HuaWei":
            return HuaWeiMobile()
        if name == "Vivo":
            return VivoMobile()

factory = MobileFactory()
huawei = factory.get_mobile("HuaWei")
vivo = factory.get_mobile("Vivo")

# 面向对象（上）完结