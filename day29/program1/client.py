import socket
from multiprocessing import Process
import time
import random
server_ip_port = ('127.0.0.1', 8080)
request_dict = {'inquire': '1'.encode('utf-8'),
                'buy': '2'.encode('utf-8')}


class User:
    def __init__(self, index):
        self.index = index

    def operate(self, request):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(server_ip_port)
        sock.send(request_dict[request])
        time.sleep(random.uniform(0.1, 0.2))  # 仿真网络延迟
        data = sock.recv(512)
        if data.decode('utf-8') == '1':
            if request == 'inquire':
                print('用户{}查看了余票数，目前还有余票'.format(self.index))
            else:
                sock.close()
                print('用户{}买到了票'.format(self.index))
            return True  # 当查看余票的请求时，表示还有票；当购买票的请求时，表示买到票了
        else:
            if request == 'inquire':
                print('用户{}查看了余票数，目前没有余票'.format(self.index))
            else:
                sock.close()
                print('用户{}没有买到票'.format(self.index))
            return False


if __name__ == '__main__':
    user_lst = []
    for i in range(1, 101):
        user_lst.append(User(i))
    p_look_list = []
    for i in user_lst:
        p = Process(target=i.operate, args=('inquire',))
        p_look_list.append(p)
        p.start()
    for p in p_look_list:
        p.join()
    p_list = []
    for i in user_lst:
        p = Process(target=i.operate, args=('buy',))
        p_list.append(p)
        p.start()
    for p in p_look_list:
        p.join()
    print('抢票结束')
