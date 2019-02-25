import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.connect(('127.0.0.1', 8081))

while True:
    msg = phone.recv(1024)
    select = input(msg.decode('utf-8')).strip()
    phone.send(select.encode('utf-8'))
    msg = phone.recv(1024).decode('utf-8')
    print(msg)
phone.close()