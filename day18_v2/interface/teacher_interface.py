from db import db_handler
import logging.config


def operate_course(course, user_data):
    teacher_message = db_handler.select('1')
    school = None
    for i in teacher_message:
        if i.name == user_data['name']:
            school = i.school
    school_message = db_handler.select('4')
    count = 0
    selected_school = None
    for i in school_message:
        if i.name == school:
            selected_school = count
        count += 1
    # 对应课程： school_message[selected_school].teachers[user_data['name']].courses[course]
    while True:
        input_operate = input("请选择要进行的操作：1.查看学生及成绩  2.录入成绩  3.修改成绩  4.保存并返回").strip()
        if input_operate == '1':
            if not school_message[selected_school].teachers[user_data['name']].courses[course]:
                print('无任何数据')
            else:
                for key in school_message[selected_school].teachers[user_data['name']].courses[course]:
                    print(key + ':' +
                          str(school_message[selected_school].teachers[user_data['name']].courses[course][key]))
        elif input_operate == '2':
            input_score = input('请依次输入学生姓名与成绩，以 姓名 成绩的格式，逐行打入')
            while input_score:
                input_score = input_score.strip().split()
                school_message[selected_school].teachers[user_data['name']].courses[course].students[input_score[0]] \
                    = input_score[1]
                input_score = input()
        elif input_operate == '3':
            input_score = input('请输入学生姓名与修改后的成绩').strip().split()
            school_message[selected_school].teachers[user_data['name']].courses[course].students[input_score[0]] \
                = input_score[1]
        elif input_operate == '4':
            db_handler.save(tuple(school_message), '4')
            logging.info('%s 老师对成绩进行了操作' % user_data['name'])
            break
        else:
            print('无效的操作')


