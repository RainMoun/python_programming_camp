# -*- coding: utf-8 -*-
import pickle
import os
from conf import setting


def create_user(user):
    if not os.path.isdir(os.path.join(setting.BASE_DB, user.name)):
        os.makedirs(os.path.join(setting.BASE_DB, user.name))
        with open(os.path.join(setting.BASE_DB, user.name, user.name + '_message.pk'), 'wb') as f:
            pickle.dump(user, f)
        return True, '用户注册完成'
    else:
        return False, '用户名已存在，用户注册失败'


def select_user(name):
    if not os.path.isdir(os.path.join(setting.BASE_DB, name)):
        return None
    else:
        with open(os.path.join(setting.BASE_DB, name, name + '_message.pk'), 'rb') as f:
            now_user = pickle.load(f)
        return now_user




