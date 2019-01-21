from lib_day18 import common
from interface import manager_interface, teacher_interface, student_interface


user_data = {
    'status': None,
    'name': None
}


def login_auth(func):
    def wrapper(*args, **kwargs):
        if not user_data['name']:
            login()
        else:
            return func(*args, **kwargs)

    return wrapper


def logout():
    user_data['status'] = None
    user_data['name'] = None


def login():
    print('登陆')
    if user_data['name']:
        print('您已经登陆了')
        return
    while True:
        name = input('请输入名字:').strip()
        if name == 'q':
            break
        password = input('请输入密码：').strip()
        flag, msg = common.login_interface(name, password, user_data)
        if flag:
            user_data['name'] = name
            print(msg)
            break
        else:
            print(msg)


def register():
    print('注册')
    if user_data['name']:
        print('您已经登陆了')
        return
    while True:
        name = input('请输入名字:').strip()
        if name == 'q':
            break
        password = input('请输入密码').strip()
        conf_password = input('请确认密码').strip()
        if password == conf_password:
            flag, msg = common.register_interface(name, password, user_data)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('两次密码不一致')


# 讲师功能函数**********************************************************************************************************
@login_auth
def query_course():  # 查看课程后可查看课程对应的学生以及录入、修改他们的分数
    course = input("请输入您要查询的课程").strip()
    teacher_interface.operate_course(course, user_data)


# 学生功能函数**********************************************************************************************************
@login_auth
def query_score():  # 查看分数时可选择对应学校、任教讲师、课程
    school = input("请输入您所在的学校").strip()
    teacher = input("请输入您所查询课程的任课老师").strip()
    course = input("请输入您要查询的课程").strip()
    msg = student_interface.query_score(school, teacher, course, user_data)
    if msg:
        print(msg)


# 管理功能函数**********************************************************************************************************
@login_auth
def create_school():
    school_name = input("请输入新建学校名字").strip()
    msg = manager_interface.create_school_interface(school_name)
    print(msg)


@login_auth
def create_course():
    school_name = input("请输入创建课程的学校名").strip()
    teacher_name = input("请输入在哪个老师名下创建课程").strip()
    course_name = input("请输入创建的课程名字").strip()
    msg = manager_interface.create_course_interface(school_name, teacher_name, course_name)
    print(msg)


@login_auth
def create_teacher():
    school_name = input("请输入创建讲师的学校名").strip()
    teacher_name = input("请输入创建的老师名字").strip()
    msg = manager_interface.create_teacher_interface(school_name, teacher_name)
    print(msg)


func_dic = {
    '1': {'1': login, '2': query_course, '3': logout},  # 查看课程后可查看课程对应的学生以及录入、修改他们的分数
    '2': {'1': login, '2': register, '3': query_score, '4': logout},  # 查看分数时可选择对应学校、任教讲师、课程
    '3': {'1': login, '2': register, '3': create_school, '4': create_course, '5': create_teacher, '6': logout}
}

fun_explain = {
    '1': {'1': '登录', '2': '查看课程', '3': '登出'},  # 查看课程后可查看课程对应的学生以及录入、修改他们的分数
    '2': {'1': '登录', '2': '注册', '3': '查询分数', '4': '登出'},  # 查看分数时可选择对应学校、任教讲师、课程
    '3': {'1': '登录', '2': '注册', '3': '创建学校', '4': '创建课程', '5': '创建讲师', '6': '登出'}
}


def run():
    while True:
        print('''请选择端口：
        1. 教师端
        2. 学生端
        3. 管理员端''')
        choice_status = input('请选择:').strip()
        user_data['status'] = choice_status
        func_dict = func_dic[choice_status]
        while True:
            for i in range(1, len(func_dict) + 1):
                print('{}. {}'.format(i, fun_explain[user_data['status']][str(i)]))
            choice_func = input('请选择:').strip()
            if choice_func in func_dict:
                func_dict[choice_func]()
            if choice_func == str(len(func_dict)):
                break


