#  1. 编写函数，（函数执行的时间是随机的） 恕在下没看懂题目的意思，单纯认为函数在某个时间段内随机执行
import time
import random


def fun():
    print("哈哈，我执行了")


time.sleep(random.uniform(1, 10))
fun()
