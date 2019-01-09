# 2
def count(s):
    s_list = list(s)
    num_digit = 0
    num_space = 0
    num_letter = 0
    num_other = 0
    for i in s_list:
        if i.isdigit():
            num_digit += 1
        elif i.isalpha():
            num_letter +=1
        elif i == ' ':
            num_space += 1
        else:
            num_other += 1
    return num_digit, num_space, num_letter, num_other


# 3
def more_than_5(user_input):
    return len(user_input) > 5


# 4
def function_3(lst):
    return lst[: 2] if len(lst) > 2 else lst


# 5
def function_4(lst):
    result = []
    for i in range(1, len(lst), 2):
        result.append(lst[i])
    return result


# 6
def function_6(dict_input):
    for i in dict_input:
        dict_input[i] = dict_input[i] if len(dict_input[i]) <= 2 else dict_input[i][: 2]
    return dict_input