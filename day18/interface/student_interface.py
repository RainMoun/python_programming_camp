# -*- coding: utf-8 -*-
from db import data_interface
from lib_project import common
from conf import settings


def operate(name):
    operation_list = [-1, "查看分数", '退出登录']
    operation_fun = [-1, query_score]
    while 1:
        for i in range(1, len(operation_list)):
            print("{}. {}".format(i, operation_list[i]))
        selected_operation = int(input("请选择您所要执行的操作"))
        if selected_operation == len(operation_fun):
            print("您已退出系统，再见~！")
            break
        else:
            operation_fun[selected_operation](name)


def query_score(name):
    score_lst = data_interface.read_score()
    selected_school = input("请输入您的学校")
    selected_teacher = input("请输入您的课程讲师")
    selected_course = input("请输入您所查询的课程")
    if name not in score_lst[selected_school][selected_teacher][selected_course].keys():
        print('成绩未录入')
    else:
        print(score_lst[selected_school][selected_teacher][selected_course][name])


def main():
    user = None
    while not user:
        input_begin = input("welcome, please input l for login and r for register").strip()
        if input_begin == 'l':
            user = common.login(settings.teacher_db)
        elif input_begin == 'r':
            user = common.register(settings.teacher_db)
    operate(user)


if __name__ == '__main__':
    main()