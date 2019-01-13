from lib_project.common import login, register, operation


def main():
    user = None
    while not user:
        input_begin = input("welcome, please input l for login and r for register").strip()
        if input_begin == 'l':
            user = login()
        elif input_begin == 'r':
            user = register()
    while True:
        tags = operation(user)
        if not tags:
            print("you exit successfully")
            break


if __name__ == '__main__':  # begin
    main()


