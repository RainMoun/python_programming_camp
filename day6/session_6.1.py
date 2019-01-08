menu_university = {
    '浙江': {
        '杭州': {
            '下沙区': {
                '杭州电子科技大学': {},
                '浙江工商大学': {},
                '浙江理工大学': {}
            },
            '西湖区': {
                '浙江大学': {},
            },
        },
        '宁波': {
            '江北区': {
                '宁波大学': {}
            },
            '鄞州区': {
                "宁波诺丁汉大学": {}
            }
        }
    }
}

sign_exit = False
while not sign_exit:
    menu = menu_university
    for key in menu.keys():
        print(key)
    choose_first = input("第一层：").strip()
    if choose_first == 'b':
        break
    elif choose_first == 'exit':
        sign_exit = True
        break
    elif choose_first in menu:
        pass
    else:
        continue
    while not sign_exit:
        menu_2 = menu[choose_first]
        for key in menu_2.keys():
            print(key)
        choose_second = input("第二层：").strip()
        if choose_second == 'b':
            break
        elif choose_second == 'exit':
            sign_exit = True
            break
        elif choose_second in menu_2:
            pass
        else:
            continue
        while not sign_exit:
            menu_3 = menu_2[choose_second]
            for key in menu_3.keys():
                print(key)
            choose_third = input("第三层：").strip()
            if choose_third == 'b':
                break
            elif choose_third == 'exit':
                sign_exit = True
                break
            elif choose_third in menu_3:
                pass
            else:
                continue
            while not sign_exit:
                menu_4 = menu_3[choose_third]
                for key in menu_4.keys():
                    print(key)
                choose_forth = input("第四层：").strip()
                if choose_forth == 'b':
                    break
                elif choose_forth == 'exit':
                    sign_exit = True
                    break
                else:
                    pass
