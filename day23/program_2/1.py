from socket import *

# 先运行这个文件
print('----欢迎来到<小鸡布丁>的聊天窗口----')
recv_socket = socket(AF_INET, SOCK_DGRAM)
recv_socket.bind(('', 8888))
while True:
    content = recv_socket.recvfrom(1024)
    print('小鸭寿司回复：%s' % (content[0].decode('utf-8')))

    data = input('小鸡布丁说：')
    recv_socket.sendto(data.encode('utf-8'), ('127.0.0.1', 9999))  # IP改成客户端（小鸭）的

recv_socket.close()