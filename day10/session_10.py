# 1.将names=['albert','james','kobe','kd']中的名字全部变大写
lst_name = ['albert', 'james', 'kobe', 'kd']
result = [i.upper() for i in lst_name]
print(result)

# 2.将names=['albert','jr_shenjing','kobe','kd']中以shenjing结尾的名字过滤掉，然后保存剩下的名字长度
names = ['albert', 'jr_shenjing', 'kobe', 'kd']
result = [i for i in names if not i.endswith('shenjing')]
print(result)

# 3.求文件a.txt中最长的行的长度（长度按字符个数算，需要使用max函数）
with open('a.txt', 'r') as f:
    print(max(len(i) for i in f.readlines()))

# 4.求文件a.txt中总共包含的字符个数？思考为何在第一次之后的n次sum求和得到的结果为0？（需要使用sum函数）
with open('a.txt', 'r') as f:
    print(sum(len(i) for i in f.readlines()))   # 为0的原因个人猜测是读取文件的指针指向了文件末尾

# 5
with open('a.txt') as f:
    g = (len(line) for line in f)
# print(sum(g))  # 报错的原因在于g仅仅是一个生成器，在调用sum函数的时候文件已经关闭，所以无法读取文件里的内容

# 6
sum_money = 0
with open('shopping.txt') as f:
    sum_money = sum(int(i.strip().split(',')[1]) * int(i.strip().split(',')[2]) for i in f)
print(sum_money)

with open('shopping.txt') as f:
    item_message = [{
        'name': i.split(',')[0],
        'price': i.split(',')[1],
        'count': int(i.split(',')[2])
    } for i in f]
print(item_message)

with open('shopping.txt') as f:
    item_message = [{
        'name': i.split(',')[0],
        'price': i.split(',')[1],
        'count': int(i.split(',')[2])
    } for i in f if int(i.split(',')[1]) > 10000]
print(item_message)