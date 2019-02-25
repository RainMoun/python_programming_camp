from socket import *

# 再运次这个文件
print('----欢迎来到<小鸭寿司>的聊天窗口----')
send_socket = socket(AF_INET, SOCK_DGRAM)
address = ('127.0.0.1', 8888)  # IP改成服务器端（小鸡）的
send_socket.bind(('', 9999))
while True:
    data = input('小鸭寿司说：')
    send_socket.sendto(data.encode('utf-8'), address)

    msg = send_socket.recvfrom(1024)
    print('小鸡布丁回复：%s' % (msg[0].decode('utf-8')))

send_socket.close()