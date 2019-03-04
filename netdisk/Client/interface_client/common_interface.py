import hashlib
from conf_client import setting
from lib_program_client import common


def login_interface(name, password, status):
    msg = setting.flag_description["login"] + "||" + str(status) + "|" + name + "|" + password
    flag, is_member = common.send_message_to_server(msg)  # 是否成功|是否是会员
    if flag:
        if status:
            now_user = common.Admin(name, password)
        else:
            now_user = common.User(name, password, is_member)
        return True, '欢迎您，' + name, now_user
    else:
        return False, '登录失败，请重试', None


def register_interface(name, password, status):
    msg = setting.flag_description["register"] + "||" + str(status) + "|" + name + "|" + password
    flag, is_member = common.send_message_to_server(msg)  # 是否成功|是否是会员
    if flag:  # 注册成功
        if status:
            now_user = common.Admin(name, password)
        else:
            now_user = common.User(name, password, is_member)
        return True, '欢迎您，' + name, now_user
    else:
        return False, '注册失败，请重试', None


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