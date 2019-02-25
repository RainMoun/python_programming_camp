from multiprocessing import Process

from lib_day23_program_2 import common
import logging.config
import socket
import setting
user_data = {
    'name': None
}


def login_auth(func):
    def wrapper(*args, **kwargs):
        if not user_data['name']:
            login()
        else:
            return func(*args, **kwargs)

    return wrapper


def logout():
    user_data['status'] = None
    user_data['name'] = None


def login():
    print('登陆')
    if user_data['name']:
        print('您已经登陆了')
        return
    while True:
        name = input('请输入名字:').strip()
        if name == 'q':
            break
        password = input('请输入密码：').strip()
        flag, msg, now_user = common.login_interface(name, password)
        if flag:
            sock = socket.socket(type=socket.SOCK_DGRAM)
            sock.bind(now_user.ip_port)
            messages = ('2||' + name).encode('utf-8')
            sock.sendto(messages, setting.ip_port)
            sock.close()
            user_data['name'] = now_user
            print(msg)
            break
        else:
            print(msg)


def register():
    print('注册')
    if user_data['name']:
        print('您已经登陆了')
        return
    while True:
        name = input('请输入名字:').strip()
        if name == 'q':
            break
        password = input('请输入密码').strip()
        conf_password = input('请确认密码').strip()
        if password == conf_password:
            flag, msg = common.register_interface(name, password)
            if flag:
                logging.info('%s 登陆' % name)
                print(msg)
                break
            else:
                print(msg)
        else:
            print('两次密码不一致')


@login_auth
def single_chat():
    friend_name = user_data['name'].find_friends()
    sock = socket.socket(type=socket.SOCK_DGRAM)
    sock.bind(user_data['name'].ip_port)
    p_wait = Process(target=wait_message, args=(sock,))
    p_wait.start()
    while True:
        message = input('To ' + friend_name + '(结束聊天请输入q):').strip()
        if message == 'q':
            p_wait.terminate()
            break
        messages = ('0||' + friend_name + '||' + message).encode('utf-8')
        sock.sendto(messages, setting.ip_port)
    sock.close()


@login_auth
def multi_person_chat():
    group_name, group_lst = user_data['name'].select_group_chat()
    sock = socket.socket(type=socket.SOCK_DGRAM)
    sock.bind(user_data['name'].ip_port)
    p_wait = Process(target=wait_message, args=(sock,))
    p_wait.start()
    while True:
        message = input('To ' + group_name + '(结束聊天请输入q):').strip()
        if message == 'q':
            p_wait.terminate()
            break
        messages = ('1||' + group_name + '||' + ' '.join(group_lst) + '||' + message).encode('utf-8')
        sock.sendto(messages, setting.ip_port)


def wait_message(sock):
    while True:
        data, addr = sock.recvfrom(1024)
        data = data.decode('utf-8')
        message = data.strip().split('||')
        print("{}:{}".format(message[0], message[1]))


func_dict = {'1': {'fun': register, 'explain': '注册'},
             '2': {'fun': login, 'explain': '登录'},
             '3': {'fun': single_chat, 'explain': '私聊'},
             '4': {'fun': multi_person_chat, 'explain': '群聊'},
             '5': {'fun': logout, 'explain': '登出'}}


def run():
    while True:
        for i in range(1, len(func_dict) + 1):
            print('{}. {}'.format(i, func_dict[str(i)]['explain']))
        choice_func = input('请选择:').strip()
        if choice_func in func_dict:
            func_dict[choice_func]['fun']()
        if choice_func == str(len(func_dict)):
            break
