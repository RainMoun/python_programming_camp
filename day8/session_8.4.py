login_success = 0


def login(fun):
    def wrapper(*args, **kwargs):
        global login_success
        if login_success == 1:
            res = fun(*args, **kwargs)
            return res
        else:
            user_password = {}
            with open('user_password.txt', 'r') as f:
                content = f.readline()
                while content:
                    user, password = content.strip().split()
                    user_password[user] = password
                    content = f.readline()
            input_user = input('user:').strip()
            input_password = input('password:').strip()
            if input_user in user_password.keys() and user_password[input_user] == input_password:
                login_success = 1
                res = fun(*args, **kwargs)
                return res
            else:
                print('login fail')
    return wrapper


@login
def hello_world():
    print('hello world!!!')


hello_world()
