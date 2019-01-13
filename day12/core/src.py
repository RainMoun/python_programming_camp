import logging
from lib_project.common import login, register, buy_item, withdraw_money, repayment, raise_money
logging.basicConfig(filename='F:/python_programming_camp/day12/log/access.log',
                    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S %p',
                    level=10)


def main():
    user = None
    while not user:
        input_begin = input("welcome, please input l for login and r for register").strip()
        if input_begin == 'l':
            user = login()
        elif input_begin == 'r':
            user = register()
    while True:
        input_operate = input("please select what you want to do, input w for Cash withdrawal, c for consumption"
                              ", r for Repayment ,rr for raise and b for back").strip()  # 取现，消费，还款，提额
        if input_operate == 'w':
            withdraw_money(user)
        elif input_operate == 'c':
            buy_item(user)
        elif input_operate == 'r':
            repayment(user)
        elif input_operate == 'rr':
            raise_money(user)
        elif input_operate == 'b':
            break


if __name__ == '__main__':  # begin
    main()


