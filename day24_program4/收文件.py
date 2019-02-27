#!/usr/local/python3/bin/python3
import socket
import os

# family type
sk = socket.socket()
address = ('127.0.0.1', 8888)
sk.bind(address)
sk.listen(3)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

while True:
    conn, addr = sk.accept()
    while True:
        data = conn.recv(1024)
        cmd, filename, filesze = str(data, 'utf8').split('|')
        path = os.path.join(BASE_DIR, 'file_upload', filename)
        filesze = int(filesze)

        f = open(path, 'ab')
        has_received = 0
        while has_received != filesze:
            data = conn.recv(1024)
            f.write(data)
            has_received += len(data)
        f.close()

sk.close()