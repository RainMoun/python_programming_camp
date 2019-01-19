# -*- coding: utf-8 -*-
import pickle
from conf import settings


class Course:  # 创建课程
    def __init__(self, name, school, cycle, price):
        self.name = name
        self.school = school
        self.cycle = cycle
        self.price = price


class Class:  # 创建班级
    def __init__(self, name, course, teacher, students=None):
        self.name = name
        self.course = course
        self.teacher = teacher
        if students is None:
            self.students = []
        else:
            self.students = list(students)


def register(db_path):  # 注册
    name = input("please enter your name:").strip()
    password = input("please enter your password:").strip()
    confirm_password = input("confirm your password:").strip()
    while password != confirm_password:
        print("input password inconsistencies,please try again")
        password = input("please enter your password:")
        confirm_password = input("confirm your password:")
    user_info = {"password": password, "ban": 0}
    with open(db_path, 'rb') as f:
        content = f.read()
    if content:
        fr = open(db_path, 'rb')
        user_list = pickle.load(fr)
        if name not in user_list.keys():
            user_list[name] = user_info
        else:
            print("existed user name")
            return None  # 如果用户名重复，则返回空
        fr.close()
    else:
        user_list = {name: user_info}
    # json_user = pickle.dumps(user_list)
    with open(db_path, "wb") as f:
        pickle.dump(user_list, f)
    return name  # 将已注册用户作为返回值


def login(db_path):
    login_user = None  # 标识登录用户，作为返回值
    error_count = 0  # 记录输入密码错误的次数
    with open(db_path, 'rb') as f:
        user_list = pickle.load(f)
    name = input("please enter your count:").strip()
    while name not in user_list.keys():  # 判断输入用户名是否在文件中
        name = input('not existed user, please check it again, if you want exit, input b').strip()
        if name == 'b':
            return login_user
    if user_list[name]['ban'] == 1:  # 判断该用户名是否被锁定
        print("sorry, you are banned")
        return login_user
    password = input("please enter your password:").strip()
    while user_list[name]['password'] != password:
        error_count += 1
        if error_count == 3:  # 达到次数3，将用户锁定
            user_list[name]['ban'] = 1
            json_user = pickle.dumps(user_list)
            with open(db_path, "wb") as f:
                f.write(json_user)
                f.close()
            print("sorry, you are banned")
            return login_user
        else:
            password = input("error, please enter your password:").strip()
    print("login success, {}".format(name))
    return name  # 将已登录用户名返回


if __name__ == '__main__':
    login(settings.manager_db)
