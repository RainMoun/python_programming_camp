with open('a.txt', 'r') as f:
    line_content = f.readlines()
now_content = []
for i in line_content:
    sub_str = i
    now_content.append(sub_str.replace('mac', 'linux'))
with open('a.txt', 'r+') as f:
    f.write(''.join(now_content))
