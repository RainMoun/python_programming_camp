import socket
ip_port = ('127.0.0.1', 8081)
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    begin = input('输入1以校对时间：').strip()
    client.sendto(begin.encode('utf-8'), ip_port)
    data, addr = client.recvfrom(512)
    print('time: ', data)