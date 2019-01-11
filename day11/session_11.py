# 1
with open('a.txt', 'r', encoding='utf-8') as f:
    lst = [{'name': i.strip().split()[0],
            'sex': i.strip().split()[1],
            'age': i.strip().split()[2],
            'salary': i.strip().split()[3]
            } for i in f]
print(lst)

# 2
print(max(lst, key=lambda x: x['salary']))

# 3
print(min(lst, key=lambda x: x['age']))

# 4
print(list(map(lambda x: {'name': x['name'].capitalize(),
                          'sex': x['sex'],
                          'age': x['age'],
                          'salary': x['salary']}, lst)))

# 5
print(list(filter(lambda x: x['name'][0] is not 'a', lst)))


# 6
def fib(a, b, n):
    if a > n:
        return
    print(a)
    fib(b, a+b, n)


fib(0, 1, 20)

# 7. 一个嵌套很多层的列表，如l=［1,2,[3,[4,5,6,[7,8,[9,10,[11,12,13,[14,15]]]]]]］，用递归取出所有的值
lst = [1, 2, [3, [4, 5, 6, [7, 8, [9, 10, [11, 12, 13, [14, 15]]]]]]]


def read(l):
    for i in l:
        if isinstance(i, int):
            print(i)
        elif isinstance(i, list):
            read(i)


read(lst)

