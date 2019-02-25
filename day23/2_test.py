import multiprocessing
import time


def func1():
    print('func1 starting!!!')
    time.sleep(3)
    print('3s func1')
    time.sleep(4)
    print('4s func1')


def func2():
    print('func2 starting!!!')
    time.sleep(1)
    print('1s func2')
    time.sleep(5)
    print('5s func2')


if __name__ == '__main__':
    p_1 = multiprocessing.Process(target=func1)
    p_2 = multiprocessing.Process(target=func2)
    p_1.start()
    p_2.start()
    print('end')