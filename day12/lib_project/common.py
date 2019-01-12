import json
import logging

from conf import settings

logging.basicConfig(filename='F:/python_programming_camp/day12/log/access.log',
                    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S %p',
                    level=10)


def register():  # 注册
    name = input("please enter your name:").strip()
    password = input("please enter your password:").strip()
    confirm_password = input("confirm your password:").strip()
    while password != confirm_password:
        print("input password inconsistencies,please try again")
        password = input("please enter your password:")
        confirm_password = input("confirm your password:")
    user_info = {"password": password, "balance": 0, "ban": 0}
    with open(settings.user_file, 'r') as f:
        content = f.read()
    if content:
        fr = open(settings.user_file)
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
    with open(settings.user_file, "w") as f:
        f.write(json_user)
        f.close()
    return name  # 将已注册用户作为返回值


def login():
    login_user = None  # 标识登录用户，作为返回值
    error_count = 0  # 记录输入密码错误的次数
    with open(settings.user_file) as f:
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
            with open(settings.user_file, "w") as f:
                f.write(json_user)
                f.close()
            print("sorry, you are banned")
            return login_user
        else:
            password = input("error, please enter your password:").strip()
    print("login success, {}".format(name))
    return name  # 将已登录用户名返回


def buy_item(user):
    with open(settings.user_file) as f:
        user_list = json.load(f)
    original_balance = user_list[user]['balance']
    print("商品列表：")
    for i in range(1, len(settings.item_price)):
        print('商品编号：' + str(i) + '  商品名称：' + settings.item_list[i] + '  商品价格：' + str(settings.item_price[i]))
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
                with open(settings.user_file, "w") as f:
                    f.write(json_user)
                    f.close()
                logging.info(user + ' consumption ' + str(original_balance - user_list[user]['balance']))
                break
        elif input_user.isdigit():
            price_item = int(input_user)  # 当前选择的商品编号
            if price_item > len(settings.item_price) or price_item <= 0:
                print("您所选商品不存在")
            else:
                if settings.item_price[price_item] <= user_list[user]['balance']:
                    user_list[user]['balance'] -= settings.item_price[price_item]
                    item_buy.append(price_item)
                else:
                    print("对不起，您的余额不足")


def withdraw_money(user):
    with open(settings.user_file) as f:
        user_list = json.load(f)
    input_cash = int(input("需要取多少钱？").strip())
    if input_cash <= user_list[user]['balance']:  # 钱数大于余额
        user_list[user]['balance'] -= input_cash
        json_user = json.dumps(user_list)
        with open(settings.user_file, "w") as f:
            f.write(json_user)
            f.close()
        logging.info(user + ' Cash withdrawal ' + str(input_cash))
    else:
        print("余额不足，请充值")


def repayment(user):
    with open(settings.user_file) as f:
        user_list = json.load(f)
    if user_list[user]['balance'] >= 0:
        print("您好，您的信用卡暂无欠款")
    else:
        input_repay = int(input("输入您偿还钱的数额："))
        user_list[user]['balance'] += input_repay
        json_user = json.dumps(user_list)
        with open(settings.user_file, "w") as f:
            f.write(json_user)
            f.close()
        logging.info(user + ' Repayment')


def raise_money(user):
    print("提额成功")
    logging.info(user + ' Raise')


