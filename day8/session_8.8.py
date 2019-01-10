fun_dict = {}


def add_dict(name):
    def swapper(fun):
        def swapper_1(*args, **kwargs):
            fun_dict[name] = fun
            res = fun(*args, **kwargs)
            return res
        return swapper_1
    return swapper


@add_dict('add_fun')
def f1(a, b):
    return a + b


@add_dict('reduce_fun')
def f2(a, b):
    return a - b


@add_dict('mul_fun')
def f3(a, b):
    return a * b


@add_dict('div_fun')
def f4(a, b):
    return a / b if b != 0 else 'Nan'


print(f1(1, 2))
print(f2(1, 2))
print(f3(1, 2))
print(f4(1, 2))
print(fun_dict)