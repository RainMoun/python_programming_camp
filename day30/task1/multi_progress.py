# 在多核CPU下多进程的执行效率
import time
from multiprocessing import Process
import threading


def func_io():  # io密集型
    time.sleep(2)
    time.sleep(1)
    time.sleep(2)


def func_cal():  # 计算密集型
    result = 0
    for num in range(1000000000):
        result += num


if __name__ == '__main__':  # 多进程和多线程下的效率对比
    # 多进程下
    start_time_process = time.time()
    p_list = []
    for i in range(10):
        if i % 2 == 0:  # 加入io密集型进程
            p = Process(target=func_io)
        else:
            p = Process(target=func_cal)
        p_list.append(p)
        p.start()
    for p in p_list:
        p.join()
    all_time_process = time.time() - start_time_process

    # 多线程下
    start_time_threading = time.time()
    t_list = []
    for i in range(10):
        if i % 2 == 0:  # 加入io密集型进程
            t = threading.Thread(target=func_io)
        else:
            t = threading.Thread(target=func_cal)
        t_list.append(t)
        t.start()
    for t in t_list:
        t.join()
    all_time_threading = time.time() - start_time_threading
    print("多进程下IO密集型与计算密集型任务共同执行了{}".format(all_time_process))
    print("多线程下IO密集型与计算密集型任务共同执行了{}".format(all_time_threading))
    # 多进程下IO密集型与计算密集型任务共同执行了80.93605494499207
    # 多线程下IO密集型与计算密集型任务共同执行了268.05171513557434
