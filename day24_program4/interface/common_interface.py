import logging.config
import hashlib
from db import db_handler
from db import models


def login_interface(name, password, status):
    now_user = db_handler.select_user(name, status)
    if now_user:
        if now_user.password == password:
            logging.info('%s 登陆' % name)
            return True, '欢迎您，' + name, now_user
        else:
            return False, '用户密码错误', None
    else:
        return False, '用户不存在', None


def register_interface(name, password, status):
    if status == 1:
        now_user = models.Admin(name, password)
    else:
        now_user = models.User(name, password)
    flag, msg = db_handler.create_user(now_user, status)
    if flag:
        if status == 1:
            role = 'admin'
        else:
            role = 'user'
        logging.info('{} {}完成注册'.format(role, name))
    return flag, msg


def get_file_md5(filename):
    my_hash = hashlib.md5()
    f = open(filename, 'rb')
    while True:
        b = f.read(8096)
        if not b:
            break
        my_hash.update(b)
    f.close()
    return my_hash.hexdigest()