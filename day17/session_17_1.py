class SlopOverError(BaseException):
    def __init__(self, number, message):
        self.number = number
        self.message = message

    def __str__(self):
        return '<%s：%s>' % (self.username, self.massage)


class Integer:
    @classmethod
    def get_num(cls):
        error_tag = 0
        try:
            input_num = input("please input a num:")
            if not input_num.isdigit():
                error_tag = 1
                print('invalid literal for int() with base 10:%s' % input_num)
                raise ValueError('invalid literal for int() with base 10:%s' % input_num)
            if int(input_num) < -2147483648 or int(input_num) > 2147483647:
                error_tag = 1
                print('ErrorMsg：%s - 越界' % input_num)
                raise SlopOverError('ErrorMsg：%s - 越界' % input_num)
        finally:
            return int(input_num) if error_tag == 0 else cls.get_num()


if __name__ == '__main__':
    input_digit = Integer().get_num()





