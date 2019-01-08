item_list = {1: "21个项目玩转深度学习", 2: "流畅的python", 3: "机器学习", 4: "统计学习方法"}
item_price = [-1, 50, 34, 68, 50]
f = open('user_password.txt')
user_password = {}
for i in f.readlines():
    user, password = i.split('|')
    if '\n' in password:
        password = password[: -1]
    user_password[user] = password
blacklist = []
f_blacklist = open('blacklist.txt')
for i in f_blacklist.readlines():
    blacklist.append(i)
f.close()
f_blacklist.close()
login_success = 0
login_error = 0
while 1:
    user_input = input("请输入用户名：").strip()
    if user_input in blacklist:
        print("对不起，您的用户名已被禁止登陆")
        break
    password_input = input("请输入密码：").strip()
    if user_input in user_password.keys():
        if user_password[user_input] == password_input:
            login_success = 1
            break
        else:
            print("用户名与密码不匹配，请重新输入")
            login_error += 1
            if login_error == 3:
                print("您的账户已被注销")
                f_blacklist = open('blacklist.txt', "a+", encoding="utf-8")
                f_blacklist.write("\n" + user_input)
                f_blacklist.close()
                break
            else:
                continue
if login_success == 1:  # 判断是否成功登陆
    wage_value = int(input("欢迎登陆 " + user_input + "请输入您的工资").strip())
    item_count = 0
    print("商品列表：")
    for i in range(1, len(item_price)):
        print('商品编号：' + str(i) + '  商品名称：' + item_list[i] + '  商品价格：' + str(item_price[i]))
    item_buy = []
    while 1:
        input_user = input("请输入您所选购的商品编号， 若结束选购，请输入b").strip()
        if input_user == 'b':
            if not item_buy:
                print('您未选购任何商品，余额为：{money}'.format(money=wage_value))
            else:
                print('您的余额为{money}， 您所选购的商品如下：'.format(money=wage_value))
                for i in item_buy:
                    print(i)
                break
        elif input_user.isdigit():
            price_item = int(input_user)  # 当前选择的商品编号
            if price_item > len(item_price) or price_item <= 0:
                print("您所选商品不存在")
            else:
                if item_price[price_item] <= wage_value:
                    wage_value -= item_price[price_item]
                    item_buy.append(price_item)
                else:
                    print("对不起，您的余额不足")

