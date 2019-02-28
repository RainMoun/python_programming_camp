import socket

from conf import setting


user_message = {}  # 在线用户字典


def user_online():  # 用户上线即在在线用户字典中添加该用户
    user_message[data[1]] = addr


def receive_single_chat_message():  # 接受到的信息为单人聊天请求
    if data[1] not in user_message.keys():
        messages = "对不起，对方未上线".encode('utf-8')
        sock.sendto(messages, addr)
    else:
        send_name = None
        for i in user_message:
            if user_message[i] == addr:
                send_name = i
        messages = (send_name + '||' + data[2]).encode('utf-8')
        sock.sendto(messages, user_message[data[1]])


def receive_group_chat_message():  # 接受到的信息为群聊请求
    group_dict = list(data[2].split())
    messages = (data[1] + '||' + data[3] + '||' + data[4]).encode('utf-8')
    for i in group_dict:
        if i in user_message.keys():
            sock.sendto(messages, user_message[i])


def user_outline():  # 用户下线即在在线用户字典中删除该用户
    del user_message[data[1]]


func_dict = {
    '0': receive_single_chat_message,  # 单人聊天请求
    '1': receive_group_chat_message,  # 群聊请求
    '2': user_online,  # 用户上线通知
    '3': user_outline  # 用户下线通知
}
if __name__ == '__main__':
    sock = socket.socket(type=socket.SOCK_DGRAM)
    sock.bind(setting.ip_port)
    print('服务器开始运行')
    # 实现通信循环
    while True:
        print('当前在线用户：', user_message)
        data, addr = sock.recvfrom(1024)
        print("Receive a message from {}:{}".format(addr, data.decode('utf-8')))
        data = data.decode('utf-8').split('||')
        func_dict[data[0]]()  # 根据接收到的包的第一个字段判断该信息类型
    sock.close()
