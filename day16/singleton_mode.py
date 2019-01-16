# 1.使用元类实现单例模式
class SingletonType(type):
    def __init__(self, class_name, class_bases, class_dic):  # 定义初始化方法
        self.__instance = None  # 定义一个类内部使用的实例
        super(SingletonType, self).__init__(class_name, class_bases, class_dic)  # 调用type类的初始化方法得到Foo类

    def __call__(self, *args, **kwargs):  # 控制类Foo的调用，即控制实例化Foo的过程
        if not self.__instance:  # 判断实例是否为空，为空则创建，否则将该实例返回
            self.__instance = super(SingletonType, self).__call__(*args, **kwargs)
        return self.__instance


class Foo(metaclass=SingletonType):
    pass


f1 = Foo()
f2 = Foo()
print(f1 is f2)


#######################################################################################################################
# 2. 使用装饰器
def build_singleton(fun):
    fun_lst = {}

    def wrapper(*args, **kwargs):
        if fun not in fun_lst:  # 如果该函数对象不在字典中
            fun_lst[fun] = fun(*args, **kwargs)
        return fun_lst[fun]
    return wrapper


@build_singleton
class Foo(metaclass=SingletonType):
    pass


f1 = Foo()
f2 = Foo()
print(f1 is f2)


#######################################################################################################################
# 3. 使用模块
from singleton_realized_by_model import singleton_by_model
s1 = singleton_by_model.foo()
s2 = singleton_by_model.foo()
print(s1 is s2)


#######################################################################################################################
# 4. 重写new方法
class SingletonByNew:
    __instance = None

    def __new__(cls):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance


s1 = SingletonByNew()
s2 = SingletonByNew()
print(s1 is s2)