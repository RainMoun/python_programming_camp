def range_v2(begin, end, step):
    while begin < end:
        yield begin
        begin += step


for i in range_v2(5, 10, 2):
    print(i)
