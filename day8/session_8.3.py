def id_check(fun):
    def wrapper(*args, **kwargs):
        user = input("your user name:")
        password = input("password: ")
        if user == 'Alice' and password == '123':
            print('login successful')
        else:
            print('login failed')
        res = fun(*args, **kwargs)
        return res
    return wrapper


@id_check
def hello_world():
    print('hello world!!!')


hello_world()