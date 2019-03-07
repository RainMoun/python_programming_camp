import socket
from multiprocessing import Process
import time
import random
server_ip_port = ('127.0.0.1', 8080)


class User:
    def __init__(self, index):
        self.index = index
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def register(self):
        self.sock.connect(server_ip_port)
        self.sock.send('1'.encode('utf-8'))  # 发送注册请求
        time.sleep(random.uniform(1, 2))
        _ = self.sock.recv(512)
        self.sock.send('2'.encode('utf-8'))  # 发送传回来的验证码
        time.sleep(random.uniform(1, 2))
        data = self.sock.recv(512).decode('utf-8')
        if data == '1':
            print('用户{}注册成功')
            self.sock.close()
        else:
            print('用户{}未注册成功')
            self.sock.close()


if __name__ == '__main__':
    user_lst = []
    for i in range(1, 101):
        user_lst.append(User(i))
    p_list = []
    for i in user_lst:
        p = Process(target=i.register)
        p_list.append(p)
        p.start()
    for p in p_list:
        p.join()
