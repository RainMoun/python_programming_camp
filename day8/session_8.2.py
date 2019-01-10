import time


def time_count(fun):

    def wrapper(*args, **kwargs):
        time_begin = time.time()
        res = fun(*args, **kwargs)
        time_end = time.time()
        print("using time:  " + str(time_end - time_begin))
        return res
    return wrapper


@time_count
def hello_world():
    time.sleep(3)
    print('hello world!!!')


hello_world()