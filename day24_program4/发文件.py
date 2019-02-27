#!/usr/local/python3/bin/python3
import socket
import os

sk = socket.socket()
address = ('127.0.0.1', 8888)
sk.connect(address)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

while True:
    inp = input('>>> ').strip()  # post | path
    cmd, path = inp.split('|')
    path = os.path.join(BASE_DIR, path)
    filename = os.path.basename(path)
    file_size = os.stat(path).st_size
    file_info = 'post|%s|%s' % (filename, file_size)
    sk.sendall(bytes(file_info, 'utf8'))

    f = open(path, 'rb')
    data = f.read(1024)

    has_sent = 0
    while has_sent != file_size:
        data = f.read(1024)
        sk.sendall(data)
        has_sent += len(data)
    f.close()
    print('upload success')

sk.close()