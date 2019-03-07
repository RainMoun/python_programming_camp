import socket
from multiprocessing import Process, JoinableQueue


def receive_msg(queue, server):
    while True:
        data, addr = server.recvfrom(512)
        data = data.decode('utf-8')
        queue.put((data, addr))


def process_msg(queue, server):
    while True:
        msg = queue.get()
        if msg[0] == '1':  # 用户请求发验证码
            server.sendto('QWER'.encode('utf-8'), msg[1])
        else:  # 用户完成注册
            server.sendto('1'.encode('utf-8'), msg[1])
        q.task_done()


if __name__ == '__main__':
    ip_port = ('127.0.0.1', 8080)
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(ip_port)
    q = JoinableQueue()
    p_receive_list = []
    for i in range(3):
        p = Process(target=receive_msg, args=(q, server,))
        p_receive_list.append(p)
        p.start()
    p_process_list = []
    for i in range(2):
        p = Process(target=process_msg, args=(q, server,))
        p.daemon = True  # 子进程变成守护进程
        p_process_list.append(p)
        p.start()
    for p in p_process_list:
        p.join()
    q.join()
    server.close()
    print('end')

