from socket import *
import struct

client = socket(AF_INET, SOCK_STREAM)
client.connect(('127.0.0.1', 8080))

while True:
    cmd = input('>>>: ').strip()
    if not cmd:
        continue
    client.send(cmd.encode('utf-8'))
    # 接受自定义报头
    res = client.recv(4)
    header = struct.unpack('i', res)[0]
    # 根据传过来的数据长度对数据进行接收
    data_size = 0
    total_data = b''
    while data_size < header:
        data_recv = client.recv(512)
        total_data += data_recv
        data_size += len(data_recv)
    print(total_data.decode('gbk'))

client.close()
