# -*- coding: utf-8 -*-
from db import data_interface
from lib_project import common
from conf import settings


def operate():
    operation_list = [-1, "创建学校", '创建课程', '创建班级', '创建老师', '退出登录']
    operation_fun = [-1, create_school, create_course, create_class, create_teacher]
    while 1:
        for i in range(1, len(operation_list)):
            print("{}. {}".format(i, operation_list[i]))
        selected_operation = int(input("请选择您所要执行的操作"))
        if selected_operation == len(operation_fun):
            print("您已退出系统，再见~！")
            break
        else:
            operation_fun[selected_operation]()


def create_school():
    print("#" * 20)
    school_lst = data_interface.read_school()
    school_name = input("请输入要创建的学校名字")
    if school_lst:
        if school_name not in school_lst.keys():
            school_lst[school_name] = {}
        else:
            print("existed school name")
    else:
        school_lst = {school_name: {}}
    data_interface.save_school(school_lst)


def create_course():
    print("#" * 20)
    school_lst = data_interface.read_school()
    for i in school_lst:
        print(i)
    selected_school = input("请输入您将要在哪所学校创建课程？")
    if selected_school not in school_lst:
        print("您所输入的学校不存在，请核实后重试")
        return
    else:
        course_lst = school_lst[selected_school]
    course_name = input("请输入要创建的课程名字")
    if course_lst:  # 如果课程不为空
        if course_name not in course_lst.keys():  # 如果要创建的课程在数据库中不存在
            course_period = input("请输入要创建的课程周期")
            course_price = input("请输入要创建的课程价格")
            course_lst[course_name] = {"课程学校": selected_school, "课程周期": course_period, "课程价格": course_price}
        else:
            print("existed course name, please try again")
    else:
        course_period = input("请输入要创建的课程周期")
        course_price = input("请输入要创建的课程价格")
        course_lst = {course_name: {"课程学校": selected_school, "课程周期": course_period, "课程价格": course_price}}
    school_lst[selected_school] = course_lst
    data_interface.save_school(school_lst)


def create_class():
    print("#" * 20)
    school_lst = data_interface.read_school()
    for i in school_lst:
        print(i)
    selected_school = input("请输入您将要在哪所学校创建班级？")
    if selected_school not in school_lst:
        print("您所输入的学校不存在，请核实后重试")
        return
    class_course = input("请输入要创建的班级课程")
    class_teacher = input("请输入要创建的班级讲师")
    class_name = school_lst + '_' + class_course + '_' + class_teacher  # 通过学校，课程，讲师来创建班级名字
    class_lst = data_interface.read_class()
    if class_lst:
        if class_name in class_lst.keys():
            print("要创建的班级已存在，请核实后重试")
            return
        else:
            class_lst[class_name] = {"班级学校": selected_school, "班级课程": class_course, "班级讲师": class_teacher}
    else:
        class_lst = {class_name: {"班级学校": selected_school, "班级课程": class_course, "班级讲师": class_teacher}}
    data_interface.save_class(class_lst)


def create_teacher():
    print("#" * 20)
    school_lst = data_interface.read_school()
    for i in school_lst:
        print(i)
    selected_school = input("请输入您将要在哪所学校创建讲师？")
    if selected_school not in school_lst:
        print("您所输入的学校不存在，请核实后重试")
        return
    score_lst = data_interface.read_score()
    if not score_lst:
        score_lst = {}
    if selected_school not in score_lst.keys():
        score_lst[selected_school] = {}
    teacher_name = input("请输入讲师姓名")
    course_lst = list(input("请输入讲师所讲授课程名，用空格隔开").split())
    print(course_lst)
    course_dict = {}
    for i in course_lst:
        course_dict[i] = {}
    if score_lst[selected_school]:
        score_lst[selected_school][teacher_name] = course_dict
    else:
        score_lst[selected_school] = {teacher_name: course_dict}
    print(score_lst)
    data_interface.save_score(score_lst)


def main():
    user = None
    while not user:
        user = common.login(settings.teacher_db)
    operate()


if __name__ == '__main__':
    main()

