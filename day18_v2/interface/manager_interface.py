from db import db_handler
from lib_day18 import common
import logging.config


def create_school_interface(name):
    school_message = db_handler.select('4')
    if school_message:
        for i in school_message:
            if i.name == name:
                return '学校已存在'
        new_school = common.School(name)
        new_school_tuple = []
        for i in school_message:
            new_school_tuple.append(i)
        new_school_tuple.append(new_school)
        db_handler.save(tuple(new_school_tuple), '4')
        logging.info('%s 学校创建了' % name)
        return '{}学校创建完成'.format(name)
    else:
        new_school = common.School(name)
        db_handler.save((new_school, ), '4')
        logging.info('%s 学校创建了' % name)
        return '{}学校创建完成'.format(name)


def create_teacher_interface(school, teacher):
    school_message = db_handler.select('4')
    selected_school = -1
    if school_message:
        count = 0
        for i in school_message:
            if i.name == school:
                selected_school = count
            count += 1
        if selected_school == -1:
            return '该学校不存在，请检查后重试'
        else:
            if teacher not in school_message[selected_school].teachers.keys():  # 在学校信息数据库中与老师信息数据库中同时创建老师信息
                new_teacher = common.Teacher(teacher, '123456', school)  # 初始密码设为123456
                school_message[selected_school].teachers[teacher] = new_teacher
                db_handler.save(tuple(school_message), '4')
                teacher_message = db_handler.select('1')
                if teacher_message:
                    new_teacher_tuple = []
                    for i in teacher_message:
                        new_teacher_tuple.append(i)
                    new_teacher_tuple.append(new_teacher)
                    db_handler.save(tuple(new_teacher_tuple), '1')
                else:
                    db_handler.save((new_teacher, ), '1')
                logging.info('%s 的 %s 老师创建了' % (school, teacher))
                return '创建完毕'
            else:
                return '该讲师已存在'
    else:
        return '数据库中无任何学校数据，请检查后重试'


def create_course_interface(school, teacher, course):
    school_message = db_handler.select('4')
    selected_school = -1
    if school_message:
        count = 0
        for i in school_message:
            if i.name == school:
                selected_school = count
            count += 1
        if selected_school == -1:
            return '该学校不存在，请检查后重试'
        else:
            if teacher in school_message[selected_school].teachers.keys():  # 在学校信息数据库中与老师信息数据库中同时创建老师信息
                if course not in school_message[selected_school].teachers[teacher].courses.keys():
                    cycle = input("请输入上课周期").strip()
                    price = input("请输入课程价格").strip()
                    new_course = common.Course(course, school, cycle, price)  # 初始密码设为123456
                    school_message[selected_school].teachers[teacher].courses[course] = new_course
                    db_handler.save(tuple(school_message), '4')
                    logging.info('%s 的 %s 老师 的 %s 课程创建了' % (school, teacher, course))
                    return '创建完毕'
                else:
                    return '该课程已存在'
            else:
                return '该讲师不存在'
    else:
        return '数据库中无任何学校数据，请检查后重试'
