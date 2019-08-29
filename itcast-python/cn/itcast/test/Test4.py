class Girl(object):
    def __init__(self):
        self.__age = 0
        self.__weight = 50

    @property
    def age(self):
        return self.__age

    @age.getter
    def age(self, value):
        self.__age = value