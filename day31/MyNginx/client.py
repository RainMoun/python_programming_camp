import socket
from multiprocessing import Process

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.connect(('127.0.0.1', 8080))


def connect_to_server(client):
    client.send('1'.encode('UTF-8'))
    msg = phone.recv(1024)
    print(msg.decode('UTF-8'))


if __name__ == '__main__':
    process_num = 10
    p_lst = []
    for i in range(process_num):
        p = Process(target=connect_to_server, args=(phone, ))
        p.start()
        p_lst.append(p)
    for p in p_lst:
        p.join()
    phone.close()