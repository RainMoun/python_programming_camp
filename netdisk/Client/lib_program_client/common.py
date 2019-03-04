import socket
import time

from conf_client import setting


class BaseRole:
    def __init__(self, name, password):
        self.name = name
        self.password = password


class Admin(BaseRole):
    def __init__(self, name, password):
        BaseRole.__init__(self, name, password)


class User(BaseRole):
    def __init__(self, name, password, is_member=0):
        super().__init__(name, password)
        self.is_member = is_member


def send_message_to_server(msg):  # 向服务器发送简短的信息，比如登录请求、注册请求、用户开通会员请求
    sk = socket.socket()
    sk.connect(setting.SERVER_ADDRESS)
    sk.sendall(msg.encode('utf-8'))
    time.sleep(0.1)
    data = sk.recv(1024)
    print(data.decode('utf-8'))
    flag, is_member = data.decode('utf-8').split('|')  # 得到服务器的反馈 1表示成功 0表示失败
    is_member = int(is_member)
    sk.close()
    return flag, is_member
