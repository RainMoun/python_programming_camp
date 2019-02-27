# -*- coding: utf-8 -*-
import pickle
import os
from conf import setting


def create_user(user, status):
    if status == 1:
        prefix = 'admin_'
    else:
        prefix = 'user_'
    if not os.path.isdir(os.path.join(setting.BASE_DB, 'user', prefix + user.name)):
        os.makedirs(os.path.join(setting.BASE_DB, 'user', prefix + user.name))
        with open(os.path.join(setting.BASE_DB, 'user', prefix + user.name, user.name + '_message.pk'), 'wb') as f:
            pickle.dump(user, f)
        return True, '用户注册完成'
    else:
        return False, '用户名已存在，用户注册失败'


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


def save_upload_file_message(file_upload):
    file_message_path = os.path.join(setting.BASE_DB, 'file_upload', 'file_message.pk')
    if not os.path.exists(file_message_path):
        f = open(os.path.join(setting.BASE_DB, 'file_upload', 'file_message.pk'), 'w')
        f.close()
    if os.path.getsize(file_message_path) > 0:
        with open(os.path.join(setting.BASE_DB, 'file_upload', 'file_message.pk'), 'rb') as f:
            file_list = pickle.load(f)
        file_list = list(file_list)
    else:
        file_list = []
    new_file_tuple = []
    for i in file_list:
        new_file_tuple.append(i)
        new_file_tuple.append(file_upload)
    with open(os.path.join(setting.BASE_DB, 'file_upload', 'file_message.pk'), 'wb') as f:
        pickle.dump(tuple(new_file_tuple), f)
