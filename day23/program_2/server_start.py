import socket
user_message = {}
sock = socket.socket(type=socket.SOCK_DGRAM)
ip_port = ('127.0.0.1', 8080)
sock.bind(ip_port)
print('服务器开始运行')
# 实现通信循环
while True:
    print(user_message)
    data, addr = sock.recvfrom(1024)
    print("Receive a message from {}:{}".format(addr, data.decode('utf-8')))
    data = data.decode('utf-8').split('||')
    if data[0] == '2':
        user_message[data[1]] = addr
    elif data[0] == '1':
        # 群聊
        group_dict = list(data[2].split())
        messages = (data[1] + '||' + data[3]).encode('utf-8')
        for i in group_dict:
            if i in user_message.keys():
                sock.sendto(messages, user_message[i])

    elif data[0] == '0':
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
    # print("Receive a message from {}:{}".format(addr, data.decode('utf-8')))
sock.close()