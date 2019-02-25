from socket import *
import subprocess
import struct

server = socket(AF_INET, SOCK_STREAM)
server.bind(('127.0.0.1', 8080))  # 127.0.0.1是本地回环地址，一般用来做测试
server.listen(5)

while True:
    conn, client_address = server.accept()  # (连接对象，客户端的ip和端口)
    print(client_address)
    while True:
        try:
            cmd = conn.recv(1024)
            obj = subprocess.Popen(cmd.decode('utf-8'),
                                   shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE
                                   )
            stdout = obj.stdout.read()
            stderr = obj.stderr.read()
            # 发送自定义报头
            header = struct.pack('i', len(stdout) + len(stderr))
            conn.send(header)
            # 发送数据部分
            conn.send(stdout)
            conn.send(stderr)
        except ConnectionResetError:
            break

    conn.close()
server.close()
