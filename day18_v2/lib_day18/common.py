import logging.config
from db import db_handler


class Manager:  # 管理员类
    def __init__(self, name, password):
        self.name = name
        self.password = password


class School:  # 学校类
    def __init__(self, name, teachers=None):
        self.name = name
        if teachers is None:
            self.teachers = {}
        else:
            self.teachers = teachers


class Teacher:  # 讲师类
    def __init__(self, name, password, school=None, courses=None):
        self.name = name
        self.password = password
        self.school = school
        if courses is None:
            self.courses = {}
        else:
            self.courses = courses


class Course:  # 课程类
    def __init__(self, name, school, cycle, price, students=None):
        self.name = name
        self.school = school
        self.cycle = cycle
        self.price = price
        if students is None:
            self.students = {}
        else:
            self.students = students


class Student:  # 讲师类
    def __init__(self, name, password, scores=None):
        self.name = name
        self.password = password
        if scores is None:
            self.scores = {}
        else:
            self.scores = scores


class_dict = {
    '1': Teacher,
    '2': Student,
    '3': Manager
}


def login_interface(name, password, user_data):
    user_dic = db_handler.select(user_data['status'])
    if user_dic:
        for i in user_dic:
            if i.name == name and i.password == password:
                return True, '登陆成功'
        return False, '用户密码错误或已经锁定'
    else:
        return False, '用户不存在'


def register_interface(name, password, user_data):
    user_dic = db_handler.select(user_data['status'])
    new_user = class_dict[user_data['status']](name, password)
    if user_dic:
        for i in user_dic:
            if i.name == name:
                return False, '用户已经存在'
        new_user_list = []
        for i in user_dic:
            new_user_list.append(i)
        new_user_list.append(new_user)
        db_handler.save(tuple(new_user_list), user_data['status'])
        logging.info('%s 注册了' % name)
        return True, '注册成功'
    else:
        db_handler.save((new_user, ), user_data['status'])
        logging.info('%s 注册了' % name)
        return True, '注册成功'


if __name__ == "__main__":
    school_1 = School("Shanghai")
    teacher_1 = Teacher('Albert', 123)
    school_2 = School("New York")
    teacher_2 = Teacher('Rain', 345)
    '''school_1.teachers.append(teacher_1)
    school_1.teachers.append(teacher_2)
    school_2.teachers.append(teacher_2)'''
    import pickle
    with open('a1b1.pk', 'wb') as f:
        pickle.dump((school_1, school_2), f)
    with open('a1b1.pk', 'rb') as f:
        school_list = pickle.load(f)
    print(school_list)
    print(school_list[0].teachers)
    print(school_list[1].teachers)