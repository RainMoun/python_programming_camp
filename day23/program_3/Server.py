import socket
import time
ip_port = ('127.0.0.1', 8081)
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(ip_port)

while True:
    fmt = '%Y/%m/%d %X'
    data, addr = server.recvfrom(512)
    print("客户端请求：", data)
    time_now = time.strftime(fmt)
    server.sendto(time_now.encode('utf-8'), addr)
