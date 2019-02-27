from interface import admin_interface, common_interface, user_interface
user_data = {
    'name': None,
    'status': 0  # 1：管理员 0：普通用户
}


def login_auth(func):
    def wrapper(*args, **kwargs):
        if not user_data['name']:
            login()
        else:
            return func(*args, **kwargs)

    return wrapper


def logout():
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
        flag, msg, now_user = common_interface.login_interface(name, password, user_data['status'])
        user_data['name'] = now_user
        if flag:

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
            flag, msg = common_interface.register_interface(name, password, user_data['status'])
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('两次密码不一致')


@login_auth
def upload_file():
    file_path = input('请输入要上传的文件路径').strip()
    flag, msg = admin_interface.upload_file_interface(user_data['name'].name, file_path)
    print(msg)


@login_auth
def download_file():
    pass


def join_membership():
    input_confirm = input("确认是否开通会员（y/n）:").strip()
    if input_confirm == 'n':
        return



admin_func_dict = {'1': {'fun': register, 'explain': '注册'},
                   '2': {'fun': login, 'explain': '登录'},
                   '3': {'fun': upload_file, 'explain': '上传文件'},
                   '4': {'fun': logout, 'explain': '登出'}}

user_func_dict = {'1': {'fun': register, 'explain': '注册'},
                  '2': {'fun': login, 'explain': '登录'},
                  '3': {'fun': download_file, 'explain': '下载文件'},
                  '4': {'fun': join_membership, 'explain': '开通会员'},
                  '5': {'fun': logout, 'explain': '登出'}}


func_dic = {
    '1': admin_func_dict,
    '2': user_func_dict
}


def run():
    while True:
        print('''
        1 管理员视图
        2 用户视图
        3 退出系统
        ''')
        choice = input('请选择:').strip()
        if choice == '3':
            break
        if choice == '1':
            user_data['status'] = 1
        func_dict = func_dic[choice]
        while True:
            for i in range(1, len(func_dict) + 1):
                print('{}. {}'.format(i, func_dict[str(i)]['explain']))
            choice_func = input('请选择:').strip()
            if choice_func in func_dict:
                func_dict[choice_func]['fun']()
            if choice_func == str(len(func_dict)):
                break
