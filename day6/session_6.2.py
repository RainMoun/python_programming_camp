item_list = {"21个项目玩转深度学习": 50, "流畅的python": 34, "机器学习": 68, "统计学习方法": 50}
f = open('user_password.txt')
user_password = {}
for i in f.readlines():
    user, password = i.split('|')
    user_password[user] = password
while 1:
    user_input = input("请输入用户名：").strip()
    s = 100

