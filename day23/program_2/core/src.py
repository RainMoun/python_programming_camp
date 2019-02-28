from multiprocessing import Process

from lib_day23_program_2 import common
import logging.config
import socket
import setting
import time
user_data = {
    'name': None,
    'client': None
}


def login_auth(func):
    def wrapper(*args, **kwargs):
        if not user_data['name']:
            login()
        else:
            return func(*args, **kwargs)

    return wrapper


def logout():
    messages = ('3||' + user_data['name'].name).encode('utf-8')
    if user_data['client']:
        user_data['client'].sendto(messages, setting.ip_port)  # 向服务器发送用户下线信息
        user_data['client'].close()
    else:
        sock = socket.socket(type=socket.SOCK_DGRAM)
        sock.bind(user_data['name'].ip_port)
        sock.sendto(messages, setting.ip_port)
        sock.close()
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
            user_data['client'] = sock
            messages = ('2||' + name).encode('utf-8')
            user_data['client'].sendto(messages, setting.ip_port)  # 向服务器发送用户登录信息
            # sock.close()
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


def receive_msg():
    # sock = socket.socket(type=socket.SOCK_DGRAM)
    # sock.bind(user_data['name'].ip_port)
    while True:
        try:
            time.sleep(0.1)
            msg, address = user_data['client'].recvfrom(1024)
            msg = msg.decode('utf-8')
            message = msg.strip().split('||')
            if message[1] == 'q':
                print('对方已下线')
                break
            print("{}:{}".format(message[0], message[1]))
            msg = input('发送消息>>:').strip()
            messages = ('0||' + message[0] + '||' + msg).encode('utf-8')
            user_data['client'].sendto(messages, address)
            if msg == 'q':
                break
        except Exception:
            break
    # sock.close()


def send_msg(friend_name):
    # sock = socket.socket(type=socket.SOCK_DGRAM)
    # sock.bind(user_data['name'].ip_port)
    while True:
        try:
            msg = input('发送信息>>:').strip()
            message = ('0||' + friend_name + '||' + msg).encode('utf-8')
            user_data['client'].sendto(message, setting.ip_port)
            if msg == 'q':
                break
            time.sleep(0.1)
            msg, address = user_data['client'].recvfrom(1024)
            msg = msg.decode('utf-8')
            message = msg.strip().split('||')
            if message[1] == 'q':
                print('对方已下线')
                break
            print("{}:{}".format(message[0], message[1]))
            send_msg(friend_name)
        except Exception:
            break
    # sock.close()


single_func_dict = {
    '1': receive_msg,
    '2': send_msg
}


@login_auth
def single_chat():
    print("""
        1 接收消息
        2 发送消息
        """)
    choice = input('请选择要进入的状态>>:').strip()
    if choice not in func_dict:
        return
    if choice == '1':
        receive_msg()
    if choice == '2':
        friend_name = user_data['name'].find_friends()
        send_msg(friend_name)

# 多线程实现
# @login_auth
# def single_chat():
#     friend_name = user_data['name'].find_friends()
#     p_wait = Process(target=wait_message)
#     p_wait.start()
#     while True:
#         message = input('To ' + friend_name + '(结束聊天请输入q):').strip()
#         if message == 'q':
#             p_wait.terminate()
#             break
#         messages = ('0||' + friend_name + '||' + message).encode('utf-8')
#         user_data['client'].sendto(messages, setting.ip_port)
#
#


# 无法在多线程中使用user_data['client']，原因不明。故关闭字典中的socket，重新创建一个
@login_auth
def multi_person_chat():
    user_data['client'].close()
    user_data['client'] = None
    sock = socket.socket(type=socket.SOCK_DGRAM)
    sock.bind(user_data['name'].ip_port)
    group_name, group_lst = user_data['name'].select_group_chat()
    p_wait = Process(target=wait_message, args=(sock, ))
    p_wait.start()
    while True:
        message = input('To ' + group_name + '(结束聊天请输入q):').strip()
        if message == 'q':
            p_wait.terminate()
            break
        messages = ('1||' + group_name + '||' + ' '.join(group_lst) + '||'
                    + user_data['name'].name + '||' + message).encode('utf-8')
        sock.sendto(messages, setting.ip_port)
        time.sleep(0.1)
    sock.close()


def wait_message(sock):
    while True:
        data, addr = sock.recvfrom(1024)
        data = data.decode('utf-8')
        message = data.strip().split('||')
        print("from group {} {}:{}".format(message[0], message[1], message[2]))


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
