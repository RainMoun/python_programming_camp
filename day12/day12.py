import logging
import json
logging.basicConfig(filename='access.log',
                    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S %p',
                    level=10)

item_list = {1: "21个项目玩转深度学习", 2: "流畅的python", 3: "机器学习", 4: "统计学习方法"}
item_price = [-1, 50, 34, 68, 50]
user_password_file = 'user_password.txt'


def register():  # 注册
    name = input("please enter your name:").strip()
    password = input("please enter your password:").strip()
    confirm_password = input("confirm your password:").strip()
    while password != confirm_password:
        print("input password inconsistencies,please try again")
        password = input("please enter your password:")
        confirm_password = input("confirm your password:")
    user_info = {"password": password, "balance": 0, "ban": 0}
    with open('user_info.json', 'r') as f:
        content = f.read()
    if content:
        fr = open('user_info.json')
        user_list = json.load(fr)
        if name not in user_list.keys():
            user_list[name] = user_info
        else:
            print("existed user name")
            return None  # 如果用户名重复，则返回空
        fr.close()
    else:
        user_list = {name: user_info}
    json_user = json.dumps(user_list)
    with open('user_info.json', "w") as f:
        f.write(json_user)
        f.close()
    return name  # 将已注册用户作为返回值


def login():
    login_user = None  # 标识登录用户，作为返回值
    error_count = 0  # 记录输入密码错误的次数
    with open('user_info.json') as f:
        user_list = json.load(f)
    name = input("please enter your count:").strip()
    while name not in user_list.keys():  # 判断输入用户名是否在文件中
        name = input('not existed user, please check it again, if you want exit, input b').strip()
        if name == 'b':
            return login_user
    if user_list[name]['ban'] == 1:  # 判断该用户名是否被锁定
        print("sorry, you are banned")
        return login_user
    password = input("please enter your password:").strip()
    while user_list[name]['password'] != password:
        error_count += 1
        if error_count == 3:  # 达到次数3，将用户锁定
            user_list[name]['ban'] = 1
            json_user = json.dumps(user_list)
            with open('user_info.json', "w") as f:
                f.write(json_user)
                f.close()
            print("sorry, you are banned")
            return login_user
        else:
            password = input("error, please enter your password:").strip()
    print("login success, {}".format(name))
    return name  # 将已登录用户名返回


def main():
    user = None
    while not user:
        input_begin = input("welcome, please input l for login and r for register").strip()
        if input_begin == 'l':
            user = login()
        elif input_begin == 'r':
            user = register()
    with open('user_info.json') as f:
        user_list = json.load(f)
    while True:
        input_operate = input("please select what you want to do, input w for Cash withdrawal, c for consumption"
                              ", r for Repayment ,rr for raise and b for back").strip()  # 取现，消费，还款，提额
        if input_operate == 'w':
            input_cash = int(input("需要取多少钱？").strip())
            if input_cash <= user_list[user]['balance']:  # 钱数大于余额
                user_list[user]['balance'] -= input_cash
                json_user = json.dumps(user_list)
                with open('user_info.json', "w") as f:
                    f.write(json_user)
                    f.close()
                logging.info(user + ' Cash withdrawal ' + str(input_cash))
            else:
                print("余额不足，请充值")
        elif input_operate == 'c':
            original_balance = user_list[user]['balance']
            print("商品列表：")
            for i in range(1, len(item_price)):
                print('商品编号：' + str(i) + '  商品名称：' + item_list[i] + '  商品价格：' + str(item_price[i]))
            item_buy = []
            while 1:
                input_user = input("请输入您所选购的商品编号， 若结束选购，请输入b").strip()
                if input_user == 'b':
                    if not item_buy:
                        print('您未选购任何商品，余额为：{money}'.format(money=user_list[user]['balance']))
                    else:
                        print('您的余额为{money}， 您所选购的商品如下：'.format(money=user_list[user]['balance']))
                        for i in item_buy:
                            print(i)
                        json_user = json.dumps(user_list)
                        with open('user_info.json', "w") as f:
                            f.write(json_user)
                            f.close()
                        logging.info(user + ' consumption ' + str(original_balance - user_list[user]['balance']))
                        break
                elif input_user.isdigit():
                    price_item = int(input_user)  # 当前选择的商品编号
                    if price_item > len(item_price) or price_item <= 0:
                        print("您所选商品不存在")
                    else:
                        if item_price[price_item] <= user_list[user]['balance']:
                            user_list[user]['balance'] -= item_price[price_item]
                            item_buy.append(price_item)
                        else:
                            print("对不起，您的余额不足")
        elif input_operate == 'r':
            print("还款成功")
            logging.info(user + ' Repayment')
        elif input_operate == 'rr':
            print("提额成功")
            logging.info(user + ' Raise')
        elif input_operate == 'b':
            break





main()

