class CarMeta(type):
    def __init__(self, class_name, class_bases, class_dic):
        super(CarMeta, self).__init__(class_name, class_bases, class_dic)

    def __call__(self, *args, **kwargs):  # 调用Car类的时候由于Car类没有__call__方法，因此调用CarMeta中的__call__方法
        obj = object.__new__(self)  # 创建一个空对象
        self.__init__(obj, *args, **kwargs)  # 初始化CarMeta,等同于产生Foo类
        if 'production_date' not in dir(obj):  # 判断Foo类中是否有production_date参数，下同
            raise TypeError('请定义production_date属性')
        if 'engine_number' not in dir(obj):
            raise TypeError('请定义engine_number属性')
        if 'capacity' not in dir(obj):
            raise TypeError('请定义capacity属性')
        return obj


class Car(metaclass=CarMeta):
    def __init__(self, name, production_date, engine_number, capacity):
        self.name = name
        self.production_date = production_date
        self.engine_number = engine_number
        self.capacity = capacity


car1 = Car("五菱宏光", "2018.1.1", '12312312312', 10)