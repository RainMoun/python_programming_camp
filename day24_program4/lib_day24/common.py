import logging.config
from db import db_handler


class User:
    def __init__(self, name, password, ip_port, friends=None, group_chat=None):
        self.name = name
        self.password = password
        if friends is None:
            self.friends = []
        else:
            self.friends = friends
        if group_chat is None:
            self.group_chat = {}
        else:
            self.group_chat = group_chat
        self.ip_port = ip_port

    def find_friends(self):
        if not self.friends:
            print('对不起，您没有任何好友')
            return None
        for i in range(1, len(self.friends) + 1):
            print('{}. {}'.format(i, self.friends[i - 1]))
        while True:
            input_num = input('请输入想与之聊天的朋友序号，结束请输入q').strip()
            if input_num == 'q':
                return None
            elif 0 <= int(input_num) <= len(self.friends):
                return self.friends[int(input_num) - 1]
            else:
                print('没有该好友')

    def select_group_chat(self):
        if not self.group_chat:
            print('对不起，您没有任何群聊')
            return None, None
        else:
            for i in self.group_chat.keys():
                print("{}. 群聊成员为“{}".format(i, self.group_chat[i]))
            while True:
                input_num = input('请输入想加入的群聊，结束请输入q').strip()
                if input_num == 'q':
                    return None, None
                elif input_num in self.group_chat.keys():
                    return input_num, self.group_chat[input_num]
                else:
                    print('没有该群聊')
                    return None, None


def login_interface(name, password):
    now_user = db_handler.select_user(name)
    if now_user:
        if now_user.password == password:
            logging.info('%s 登陆' % name)
            return True, '欢迎您，' + name, now_user
        else:
            return False, '用户密码错误', None
    else:
        return False, '用户不存在', None


def register_interface(name, password):
    now_user = User(name, password)
    return db_handler.create_user(now_user)
