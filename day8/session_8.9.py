import time
import os


def logger(logfile):
    def deco(func):
        def wrapper(*args, **kwargs):
            if not os.path.exists(logfile):
                with open(logfile, 'w'):
                    pass
            res = func(*args, **kwargs)
            with open(logfile, 'w', encoding='utf-8') as f:
                f.write('%s %s run\n' % (time.strftime('%Y-%m-%d %X'), func.__name__))
            return res
        return wrapper
    return deco


@logger(logfile='func.log')
def hello_world():
    print('hello world!!!')


hello_world()
