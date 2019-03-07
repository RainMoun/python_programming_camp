import socket
from multiprocessing import Lock
import threading
import time
import random

mutex = Lock()  # 实例化锁的对象


server_ip_port = ('127.0.0.1', 8080)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(server_ip_port)
sock.listen(10)


def operate(client, address, lock):
    data = client.recv(512)
    if data.decode('utf-8') == '1':  # 用户申请查询票
        lock.acquire()
        with open("./train ticket.txt", 'r') as f:
            num = f.readline()
        if int(num) <= 0:
            client.send('0'.encode('utf-8'))
            time.sleep(random.uniform(1, 2))  # 仿真网络延迟
        else:
            client.send('1'.encode('utf-8'))
            time.sleep(random.uniform(1, 2))  # 仿真网络延迟
        lock.release()
    else:  # 用户申请买票
        lock.acquire()
        with open("./train ticket.txt", 'r') as f:
            num = f.readline()
        if int(num) <= 0:
            client.send('0'.encode('utf-8'))
            time.sleep(random.uniform(1, 2))  # 仿真网络延迟
        else:
            num = int(num) - 1
            with open("./train ticket.txt", 'w') as f:
                f.write(str(num))
            client.send('1'.encode('utf-8'))
            time.sleep(random.uniform(1, 2))  # 仿真网络延迟
        lock.release()


while True:
    client, address = sock.accept()
    thread = threading.Thread(target=operate, args=(client, address, mutex))
    thread.start()
