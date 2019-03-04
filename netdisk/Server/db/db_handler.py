# -*- coding: utf-8 -*-
import pickle
import os
import shutil
import logging.config
import time
from conf_server import setting
from interface_server import server_interface
from db import models


def create_user(user, status):
    if status == 1:
        prefix = 'admin_'
    else:
        prefix = 'user_'
    if not os.path.isdir(os.path.join(setting.BASE_DB, 'user', prefix + user.name)):
        os.makedirs(os.path.join(setting.BASE_DB, 'user', prefix + user.name))
        with open(os.path.join(setting.BASE_DB, 'user', prefix + user.name, user.name + '_message.pk'), 'wb') as f:
            pickle.dump(user, f)
        return True
    else:
        return False


def update_user(user, status):
    if status == 1:
        prefix = 'admin_'
    else:
        prefix = 'user_'
    with open(os.path.join(setting.BASE_DB, 'user', prefix + user.name, user.name + '_message.pk'), 'wb') as f:
        pickle.dump(user, f)


def select_user(name, status):
    if status == 1:
        prefix = 'admin_'
    else:
        prefix = 'user_'
    if not os.path.isdir(os.path.join(setting.BASE_DB, 'user', prefix + name)):
        return None
    else:
        with open(os.path.join(setting.BASE_DB, 'user', prefix + name, name + '_message.pk'), 'rb') as f:
            now_user = pickle.load(f)
        return now_user


def save_upload_file_message(file_upload, status, user_name):  # 管理员 status = 1 用户 status = 0
    if status == 1:
        file_message_path = os.path.join(setting.BASE_DB, 'file_upload', 'file_message.pk')
    else:
        file_message_path = os.path.join(setting.BASE_DB, 'user', 'user_' + user_name, 'file_message.pk')
    if not os.path.exists(file_message_path):
        f = open(file_message_path, 'w')
        f.close()
    if os.path.getsize(file_message_path) > 0:  # 如果文件不为空
        with open(file_message_path, 'rb') as f:
            file_list = pickle.load(f)
        file_list = list(file_list)
    else:
        file_list = []
    new_file_tuple = []
    for i in file_list:
        new_file_tuple.append(i)
    new_file_tuple.append(file_upload)
    with open(file_message_path, 'wb') as f:
        pickle.dump(tuple(new_file_tuple), f)


def is_file_exist(file_md5, status, user_name):
    if status == 1:
        file_message_path = os.path.join(setting.BASE_DB, 'file_upload', 'file_message.pk')
    else:
        file_message_path = os.path.join(setting.BASE_DB, 'user', 'user_' + user_name, 'file_message.pk')
    if not os.path.exists(file_message_path):  # 如果文件记录不存在，说明该用户从来没有上传过文件
        return False, None
    if os.path.getsize(file_message_path) > 0:  # 如果文件不为空
        with open(file_message_path, 'rb') as f:
            file_list = pickle.load(f)
        file_list = list(file_list)
        for i in file_list:
            if i.md5 == file_md5:
                return True, i.path_in_server
        return False, None
    else:
        return False, None


def upload_file_for_admin(conn, admin_name, file_name, file_size, file_md5):  # 上传文件至服务器
    flag, path_in_server = is_file_exist(file_md5, 0, admin_name)
    if flag:
        return True
    file_path = os.path.join(setting.BASE_DIR, 'db', 'file_upload')
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    path = os.path.join(setting.BASE_DIR, 'db', 'file_upload', file_name)
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
    file_md5_finish = server_interface.get_file_md5(path)
    if file_md5_finish == file_md5:
        file_upload = models.File(file_name, file_size, file_md5, path, admin_name)
        save_upload_file_message(file_upload, 1, admin_name)
        logging.info('{} upload {}, the md5 is {}'.format(admin_name, file_name, file_md5))
        return True
    else:
        return False


def file_copy(original_path, target_path):  # 如果用户存在相同文件，就将该文件拷贝到用户指定的路径
    if not os.path.isfile(original_path):
        return False
    else:
        shutil.copyfile(original_path, target_path)  # 复制文件
        return True


def upload_file_for_user(conn, user_name, file_name, file_size, file_md5, upload_file_path):
    file_path = os.path.join(setting.BASE_DIR, 'db', 'user', 'user_' + user_name, 'upload_files')
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    path = os.path.join(file_path, upload_file_path)
    if not os.path.exists(path):
        os.makedirs(path)
    path = os.path.join(path, file_name)
    flag, path_in_server = is_file_exist(file_md5, 0, user_name)
    if flag:
        flag_copy = file_copy(path_in_server, path)
        if flag_copy:
            msg = '1'.encode('utf-8')
            conn.send(msg)
            return True
        else:
            return False
    msg = '0'.encode('utf-8')
    conn.send(msg)
    if not os.path.exists(path):  # 创建空文件
        f = open(path, 'w')
        f.close()
    f = open(path, 'ab')
    has_received = 0
    while has_received != file_size:
        data_once = conn.recv(1024)
        f.write(data_once)
        has_received += len(data_once)
        # 发送传输进度
        process_rate = int((has_received / file_size) * 1000)
        msg = str(process_rate).encode('utf-8')
        conn.send(msg)
    f.close()
    file_md5_finish = server_interface.get_file_md5(path)
    if file_md5_finish == file_md5:
        file_upload = models.File(file_name, file_size, file_md5, path, user_name)
        save_upload_file_message(file_upload, 0, user_name)
        logging.info('{} upload {}, the md5 is {}'.format(user_name, file_name, file_md5))
        return True
    else:
        return False


def show_user_files(user_name):
    file_message_path = os.path.join(setting.BASE_DB, 'user', 'user_' + user_name, 'file_message.pk')
    if not os.path.exists(file_message_path):
        return []
    if os.path.getsize(file_message_path) > 0:
        with open(file_message_path, 'rb') as f:
            file_list = pickle.load(f)
        return list(file_list)
    else:
        return []


def show_online_files():
    file_message_path = os.path.join(setting.BASE_DB, 'file_upload', 'file_message.pk')
    if not os.path.exists(file_message_path):
        return []
    if os.path.getsize(file_message_path) > 0:
        with open(file_message_path, 'rb') as f:
            file_list = pickle.load(f)
        return list(file_list)
    else:
        return []


def download_file(conn, file, is_member):
    msg = "{}|{}|{}".format(file.name, file.size, file.md5)
    conn.send(msg.encode('utf-8'))
    f = open(file.path_in_server, 'rb')
    has_sent = 0
    while has_sent != file.size:
        time_1 = time.time()
        data = f.read(1024)
        conn.sendall(data)
        has_sent += len(data)
        time_2 = time.time()
        if is_member == 0:
            time.sleep(time_2 - time_1)  # 如果不是会员，上传文件时需要花费双倍的时间
    f.close()


def join_member(user_name):
    with open(os.path.join(setting.BASE_DB, 'user', 'user_' + user_name, user_name + '_message.pk'), 'rb') as f:
        now_user = pickle.load(f)
    now_user.is_member = 1
    with open(os.path.join(setting.BASE_DB, 'user', 'user_' + user_name, user_name + '_message.pk'), 'wb') as f:
        pickle.dump(now_user, f)
