import socket
import os
from conf import setting
from interface import common_interface
from db import models, db_handler
import logging.config


def upload_file():  # 接收文件
    file_path = os.path.join(BASE_DIR, 'db', 'file_upload')
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    path = os.path.join(BASE_DIR, 'db', 'file_upload', file_name)
    if not os.path.exists(path):
        f = open(path, 'w')
        f.close()
    f = open(path, 'ab')
    has_received = 0
    while has_received != file_size:
        data_once = conn.recv(1024)
        f.write(data_once)
        has_received += len(data_once)
    f.close()
    file_md5_finish = common_interface.get_file_md5(path)
    if file_md5_finish == file_md5:
        file_upload = models.File(file_name, file_size, file_md5, admin_name)
        db_handler.save_upload_file_message(file_upload)
        logging.info('{} upload {}, the md5 is {}'.format(admin_name, file_name, file_md5))
    print('{} upload {}, the md5 is {}'.format(admin_name, file_name, file_md5))


func_dict = {
    'post': upload_file
}

if __name__ == '__main__':
    sk = socket.socket()
    sk.bind(setting.SERVER_ADDRESS)
    sk.listen(3)
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    while True:
        conn, addr = sk.accept()
        while True:
            data = conn.recv(1024)
            print(data.decode('utf-8'))
            flag, admin_name, file_name, file_size, file_md5 = data.decode('utf-8').split('|')
            file_size = int(file_size)
            func_dict[flag]()
            break
    sk.close()

