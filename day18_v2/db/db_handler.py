# -*- coding: utf-8 -*-
import pickle
import os

from conf import setting


def select(status):
    member_path = {
        '1': setting.teacher_db,
        '2': setting.student_db,
        '3': setting.manager_db,
        '4': setting.school_message_db
    }
    if os.path.getsize(member_path[status]) > 0:
        with open(member_path[status], 'rb') as f:
            member_list = pickle.load(f)
        return list(member_list)  # 返回成员类的列表
    else:
        return None


def save(member_lst, status):  # 输入成员类的元组
    member_path = {
        '1': setting.teacher_db,
        '2': setting.student_db,
        '3': setting.manager_db,
        '4': setting.school_message_db
    }
    with open(member_path[status], 'wb') as f:
        pickle.dump(member_lst, f)
