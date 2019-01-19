# -*- coding: utf-8 -*-
from db import data_interface
from lib_project import common
from conf import settings


def operate(name):
    operation_list = [-1, "录入分数", '修改分数', '退出登录']
    operation_fun = [-1, input_score, change_score]
    while 1:
        for i in range(1, len(operation_list)):
            print("{}. {}".format(i, operation_list[i]))
        selected_operation = int(input("请选择您所要执行的操作"))
        if selected_operation == len(operation_fun):
            print("您已退出系统，再见~！")
            break
        else:
            operation_fun[selected_operation](name)


def input_score(name):
    score_lst = data_interface.read_score()
    selected_school = input("请输入您所任教的学校")
    if name not in score_lst[selected_school].keys():
        print("您不在该所学校任教，请核实后重试")
        return
    for i in score_lst[selected_school][name].keys():
        print(i)
    selected_course = input("请输入您所要录入成绩的科目")
    while selected_course not in score_lst[selected_school][name].keys():
        selected_course = input("您未教授此课，请重新输入您所要录入成绩的科目")
    course_lst = {}
    name_score = input("输入格式：姓名 成绩 输入b以停止输入成绩")
    while name_score != 'b':
        name_score = list(name_score.split())
        course_lst[name_score[0]] = name_score[1]
        name_score = input("输入格式：姓名 成绩 输入b以停止输入成绩")
    score_lst[selected_school][name][selected_course] = course_lst
    data_interface.save_score(score_lst)


def change_score(name):
    score_lst = data_interface.read_score()
    selected_school = input("请输入您所任教的学校")
    if name not in score_lst[selected_school].keys():
        print("您不在该所学校任教，请核实后重试")
        return
    for i in score_lst[selected_school][name].keys():
        print(i)
    selected_course = input("请输入您所要录入成绩的科目")
    while selected_course not in score_lst[selected_school][name].keys():
        selected_course = input("您未教授此课，请重新输入您所要修改成绩的科目")
    course_lst = score_lst[selected_school][name][selected_course]
    if not course_lst:
        print('未录入任何成绩，请核实后再试')
        return
    name_input = input("请输入要修改成绩的学生姓名 输入b以停止修改成绩")
    while name_input != 'b':
        if name_input not in score_lst[selected_school][name][selected_course].keys():
            print("该学生没有对应成绩")
        else:
            score_lst[selected_school][name][selected_course][name_input] = input("请输入修改后的成绩")
        name_input = input("请输入要修改成绩的学生姓名 输入b以停止修改成绩")
    data_interface.save_score(score_lst)


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