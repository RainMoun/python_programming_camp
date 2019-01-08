age = 13
count = 0
while 1:
    print("请猜一下我的年龄：")
    age_input = int(input())
    if age_input == age:
        print("恭喜您猜对了")
        break
    elif age_input > age:
        print("您猜的太大了")
    else:
        print("您猜的太小了")
    count += 1
    if count == 3:
        count = 0
        print("是否继续游戏？输入Y/N")
        if input() == 'Y' or 'y':
            pass
        else:
            break
