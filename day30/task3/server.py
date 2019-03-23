import socket
import os

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.bind(('127.0.0.1', 8081))
phone.listen(5)

print('server start!!!')
while True:
    conn, client_address = phone.accept()
    while True:
        try:
            conn.send((os.getcwd() + '>').encode('utf-8'))
            msg = conn.recv(1024).decode('utf-8')
            print(msg)
            d = os.popen(msg)
            conn.send(d.read().encode('utf-8'))
        except Exception:
            break
    conn.close()
phone.close()