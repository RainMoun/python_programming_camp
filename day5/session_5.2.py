# 每一行内容分别为商品名字，价钱，个数，求出本次购物花费的总钱数
item_name = []
item_price = []
item_num = []
with open('a.txt', 'r') as f:
    line_content = f.readline().strip().split()
    while line_content:
        item_name.append(line_content[0])
        item_price.append(int(line_content[1]))
        item_num.append(int(line_content[2]))
        line_content = f.readline().strip().split()
money_sum = 0
for i in range(len(item_price)):
    money_sum += item_price[i] * item_num[i]
print(money_sum)