# 1）
msg_dic = {
    'apple': 10,
    'tesla': 100000,
    'mac': 3000,
    'lenovo': 30000,
    'chicken': 10,
}
goods_l = []
while True:
    for key, item in msg_dic.items():
        print('name:{} price:{}'.format(key, item))
    choice = input('请输入商品: ').strip()
    if not choice or choice not in msg_dic:
        continue
    count = input('请输入您需购买的数量>>: ').strip()
    if not count.isdigit():
        continue
    goods_l.append((choice, msg_dic[choice], count))
    print(goods_l)
# 2）
data = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
result = {"key_1": [], "key_2": []}
for i in data:
    if i > 66:
        result["key_1"].append(i)
    else:
        result["key_2"].append(i)
print(result)
