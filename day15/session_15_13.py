import abc


class Pet:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @abc.abstractmethod
    def eat(self):
        print("eating......")


class Pig(Pet):
    def __init__(self, name, type_pet):
        super().__init__(name)
        self.__type = type_pet

    @property
    def type(self):
        return self.__type

    def eat(self):
        super().eat()
        print("哼...哼...哼...")


class Cat(Pet):
    def __init__(self, name, type_pet):
        super().__init__(name)
        self.__type = type_pet

    @property
    def type(self):
        return self.__type

    def eat(self):
        super().eat()
        print("喵...喵...喵...")


class Dog(Pet):
    def __init__(self, name, type_pet):
        super().__init__(name)
        self.__type = type_pet

    @property
    def type(self):
        return self.__type

    def eat(self):
        super().eat()
        print("汪...汪...汪...")


class Master:
    def __init__(self, name, house_pet):
        self.__name = name
        self.__pet = house_pet

    def feed(self):
        print("{} 主人准备好宠物粮食".format(self.__name))
        print("{}的{}来进食".format(self.__pet.type, self.__pet.name))
        self.__pet.eat()


if __name__ == '__main__':
    dog1 = Dog("发财", "中华田园犬")
    cat1 = Cat("加菲猫", "橘猫")
    pig1 = Pig("飞天猪", "宠物猪")
    master_1 = Master("Kobe", dog1)
    master_2 = Master("Antetokounmpo", cat1)
    master_3 = Master("John", pig1)
    master_1.feed()
    print("#" * 20)
    master_2.feed()
    print("#" * 20)
    master_3.feed()
