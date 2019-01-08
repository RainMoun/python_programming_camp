user_password = {"Lily": 123, "John": 321, "Alice": 213}
error_count = 0
while 1:
    print("请输入用户名：")
    user_name = input()
    if user_name not in user_password.keys():
        print("未注册的用户名")
        continue
    while 1:
        print("请输入密码：")
        password = input()
        if user_password[user_name] == password:
            print("欢迎回来，｛｝".format(user_name))
            break
        else:
            error_count += 1
            print("密码错误")
            if error_count == 3:
                print("由于输入密码错误次数过多，您的账号已被注销")
                user_password.pop(user_name)
                break
    break
