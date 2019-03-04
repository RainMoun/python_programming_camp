import os
import socket
import time
from interface_client import common_interface
from conf_client import setting


def upload_file_interface(user_name, file_path):  # 参数为user类 本地文件地址
    if not os.path.isfile(file_path):
        return False, '文件不存在'
    file_path_lst = file_path.split('/')
    file_name = file_path_lst[-1]
    file_size = os.path.getsize(file_path)
    file_md5 = common_interface.get_file_md5(file_path)
    upload_file_path = input("请输入想要保存在网盘中的文件夹路径").strip()
    sk = socket.socket()
    sk.connect(setting.SERVER_ADDRESS)
    file_info = '5||%s|%s|%s|%s|%s' % (user_name.name, file_name, file_size, file_md5, upload_file_path)
    sk.sendall(file_info.encode('utf-8'))
    time.sleep(1)
    is_exist_flag = sk.recv(1024)
    is_exist_flag = int(is_exist_flag.decode('utf-8'))
    if is_exist_flag == 1:  # 探查文件是否已经存在
        sk.close()
        return True, '文件传输成功'
    f = open(file_path, 'rb')
    has_sent = 0
    while has_sent != file_size:
        time_1 = time.time()
        data = f.read(1024)
        sk.sendall(data)
        has_sent += len(data)
        process_rate = sk.recv(1024)
        process_rate = int(process_rate.decode('utf-8'))
        print("进度:" + "#" * (process_rate // 20) + "{}%".format(process_rate / 10))
        time_2 = time.time()
        if user_name.is_member == 0:
            time.sleep(time_2 - time_1)
            print("wait...")
            time.sleep(time_2 - time_1)  # 如果不是会员，上传文件时需要花费三倍的时间
    f.close()
    sk.close()
    print('upload success')
    return True, '文件传输成功'


def download_file_interface(user_name):
    sk = socket.socket()
    sk.connect(setting.SERVER_ADDRESS)
    msg = ('3||' + user_name.name + '|' + str(user_name.is_member)).encode('utf-8')
    sk.sendall(msg)
    time.sleep(1)
    file_list = sk.recv(1024)
    file_list = file_list.decode('utf-8')
    flag, user_files_list, online_files_list = file_list.split("||")
    if flag == '0':
        return False, '没有任何文件可供下载'
    user_files_list = user_files_list.split('|')
    online_files_list = online_files_list.split('|')
    input_select = None
    while input_select != '0' and input_select != '1':
        input_select = input("您想要下载自己网盘上的内容（请输入0）还是共享网盘上的内容（请输入1）").strip()
    if input_select == '0':
        if not user_files_list[0]:
            return False, '没有任何文件可供下载'
        count = 1
        for i in user_files_list:
            print('{}. {}'.format(count, i))
            count += 1
        input_file = input("您想下载哪个文件，输入序号即可").strip()
        input_file = '0|' + str(int(input_file) - 1)
        input_file = input_file.encode('utf-8')
        sk.sendall(input_file)
    else:
        if not online_files_list[0]:
            return False, '没有任何文件可供下载'
        count = 1
        for i in online_files_list:
            print('{}. {}'.format(count, i))
            count += 1
        input_file = input("您想下载哪个文件，输入序号即可").strip()
        input_file = '1|' + str(int(input_file) - 1)
        input_file = input_file.encode('utf-8')
        sk.sendall(input_file)
    # 获取文件名|文件长度|md5值
    data = sk.recv(1024)
    data = data.decode('utf-8')
    file_name, file_size, file_md5 = data.split('|')
    file_size = int(file_size)
    save_path = input("请选择文件夹以保存该文件").strip()
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    path = os.path.join(save_path, file_name)
    if not os.path.exists(path):
        f = open(path, 'w')
        f.close()
    f = open(path, 'ab')
    has_received = 0
    while has_received != file_size:
        data_once = sk.recv(1024)
        f.write(data_once)
        has_received += len(data_once)
        process_rate = int((has_received / file_size) * 1000)
        print("进度:" + "#" * int(process_rate // 20) + "{}%".format(process_rate / 10))
    f.close()
    file_md5_finish = common_interface.get_file_md5(path)
    if file_md5_finish == file_md5:
        return True, '文件下载成功'
    else:
        return False, '文件传输时已损坏，请重新下载'


def join_membership_interface(user_name):
    sk = socket.socket()
    sk.connect(setting.SERVER_ADDRESS)
    msg = ('6||' + user_name.name).encode('utf-8')
    sk.sendall(msg)
    time.sleep(1)
    flag = int(sk.recv(1024).decode('utf-8'))
    if flag:
        return "开通会员成功"
    else:
        return "开通会员失败"
