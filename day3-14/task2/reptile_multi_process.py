import requests
import re
from threading import Thread, Lock
from multiprocessing import JoinableQueue


def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0(Macintosh;Intel Mac OS X10_13_3) AppleWebKit/537.36(KHTML, like Gecko)'
                      'Chrome/65.0.3325.162 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None


def find_page_content(page, queue):  # 只能读取第一页的信息
    if page == 1:
        suffix = ''
    else:
        suffix = '#p{}'.format(page)
    url = 'https://www.cnblogs.com/' + suffix
    html = get_one_page(url)
    pattern = re.compile('<h3>.*?href="(.*?)".*?target.*?>(.*?)</a>', re.S)
    items = re.findall(pattern, html)
    print(items)
    content = []
    for i in items:
        pattern = re.compile('.*?python.*?', flags=re.IGNORECASE)
        item = re.findall(pattern, i[1])
        if item:
            content.append(i)
    if content:
        queue.put(content)


def save_content(queue):
    while True:
        content = queue.get()
        if content is None:
            break
        with open('./python.txt', 'a+') as fp:
            for i in content:
                fp.write("标题： {}  网址： {}\n".format(i[1], i[0]))
        queue.task_done()


if __name__ == '__main__':
    mutex = Lock()
    q = JoinableQueue()
    t_receive_list = []
    for j in range(1, 11):
        t = Thread(target=find_page_content, args=(j, q,))
        t_receive_list.append(t)
        t.start()
    t_process_list = []
    for j in range(2):
        t = Thread(target=save_content, args=(q,))
        t.daemon = True  # 子进程变成守护进程
        t_process_list.append(t)
        t.start()
    for t in t_receive_list:
        t.join()
    q.join()
    print('end')
    # url = 'https://www.cnblogs.com/#p3'
    # html = get_one_page(url)
    # pattern = re.compile('<h3>.*?href="(.*?)".*?target.*?>(.*?)</a>', re.S)
    # items = re.findall(pattern, html)
    # print(items)
