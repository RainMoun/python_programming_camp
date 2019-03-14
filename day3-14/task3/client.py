from threading import Event, current_thread, Thread
import time
import inspect
import ctypes

event = Event()


def check():
    print("{}检测服务器是否正常运行".format(current_thread().name))
    # 检测服务器是否正常
    time.sleep(10)
    event.set()


def connect():
    connect_time = 0
    while connect_time < 3:
        print("{}等待连接".format(current_thread().name))
        event.wait(1)
        print("{}开始连接".format(current_thread().name))
        connect_time += 1


if __name__ == '__main__':
    t_lst = []
    for _ in range(3):
        t = Thread(target=connect)
        t_lst.append(t)
    for t in t_lst:
        t.start()
    c1 = Thread(target=check)
    c1.start()
    for t in t_lst:
        t.join()
    if not event.is_set():
        print("您的网速过慢，请稍后再试")