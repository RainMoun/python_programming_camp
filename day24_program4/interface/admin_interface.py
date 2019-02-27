import os
import socket
import time
from interface import common_interface
from conf import setting


def upload_file_interface(admin_name, file_path):  # 将本地文件上传至服务器
    if not os.path.isfile(file_path):
        return False, '文件不存在'
    file_path_lst = file_path.split('/')
    file_name = file_path_lst[-1]
    file_size = os.path.getsize(file_path)
    file_md5 = common_interface.get_file_md5(file_path)
    # file = models.File(file_name, file_size, file_md5)
    sk = socket.socket()
    sk.connect(setting.SERVER_ADDRESS)
    file_info = 'post|%s|%s|%s|%s' % (admin_name, file_name, file_size, file_md5)
    sk.sendall(file_info.encode('utf-8'))
    time.sleep(1)
    f = open(file_path, 'rb')
    has_sent = 0
    while has_sent != file_size:
        data = f.read(1024)
        sk.sendall(data)
        has_sent += len(data)
    f.close()
    sk.close()
    print('upload success')
    return True, '文件传输成功'
