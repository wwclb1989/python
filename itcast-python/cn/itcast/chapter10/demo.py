# 第10章 面向对象（上）
# 类的定义和使用
class Dog(object):
    legs = 4
    def description(self, dog_name):
        print("狗的名字是%s"%dog_name)

# 在类中定义的方法带一个默认参数self，指的是对象本身
# 创建对象：对象名 = 类名()

# 属性包括类属性和对象属性
# 类属性定义在类的内部，方法的外部，类属性的值可以通过类和对象来访问，但是只能通过类来修改，包括直接使用类属性修改或者在类方法中修改
# 对象属性可以在类定义的方法里添加，也可以在调用实例的代码里添加
# 使用del可以删除对象属性
# 构造方法__init___(), 析构方法__del__()，分别在类创建和销毁的时候调用
# 对象方法是在类中定义的，以关键字self作为第一个参数的方法，类调用对象方法的时候需要传入类或者该类对象作为参数
# 类方法是使用修饰器@classmethod修饰的方法，第一个参数表示类本身，类和对象都可以调用
# 静态方法是使用@staticmethod进行修饰的方法，类和对象都可以调用
class Employee:
    __company = '黑马'
emp = Employee()
# 变量名称前加了__的类属性是私有属性，加了__的方法是私有方法，直接访问会报错
# print(emp.__company)
# 使用命名混淆后就可以访问成功了
print(emp._Employee__company)
# 使用@property装饰器访问私有属性
class Girl(object):
    def __init__(self):
        self.__age = 0
        self.__weight = 50

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @property
    def weight(self):
        return self.__weight

    @age.deleter
    def age(self):
        del self.__age

lily = Girl()
lily.age = 25
print(lily.age)
print(lily.weight)
del lily.age
# lily.weight = 55