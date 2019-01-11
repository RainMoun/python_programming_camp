def init(fun):
    def swapper(*args, **kwargs):
        res = fun(*args, **kwargs)
        next(res)
        return res
    return swapper


@init
def print_num(begin, end):
    while begin < end:
        yield begin
        begin += 1


s = print_num(2, 9)
print(next(s))
print(next(s))
print(next(s))
