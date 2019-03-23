import socket
from multiprocessing import Process
from threading import Thread, Lock
import gevent


client_num = 0


def open_thread(lock, connect):
    thread_list = []
    for _ in range(100):
        t = Thread(target=open_yield, args=(lock, connect, ))
        thread_list.append(t)
        t.start()
    for t in thread_list:
        t.join()


def open_yield(lock, connect):
    g_lst = []
    for _ in range(5):
        g = gevent.spawn(recv_msg_from_client, (lock, connect,))
        g_lst.append(g)
    gevent.joinall(g_lst)


def recv_msg_from_client(lock, connect):
    lock.acquire()
    global client_num
    connect.send(('收到您的请求，{}'.format(client_num)).encode('UTF-8'))
    client_num += 1
    lock.release()
    connect.close()


if __name__ == '__main__':
    mutex = Lock()
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 8080))
    server.listen(5)
    process_num = 10
    p_lst = []
    while True:
        conn, addr = server.accept()
        for _ in range(process_num):
            p = Process(target=open_thread, args=(mutex, conn, ))
            p.start()
            p_lst.append(p)
        for p in p_lst:
            p.join()