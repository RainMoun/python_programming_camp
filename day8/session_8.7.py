import requests
import os


def read_cache(fun):
    def wrapper(*args, **kwargs):
        if os.path.exists('./cache_folder/1.txt'):
            f = open('./cache_folder/1.txt', 'r')
            content = f.readlines()
            f.close()
            if len(content) > 0:
                return content
            else:
                res = fun(*args, **kwargs)
                f = open('./cache_folder/1.txt', 'w', encoding='utf-8')
                f.write(res)
                f.close()
                return res
        else:
            res = fun(*args, **kwargs)
            f = open('./cache_folder/1.txt', 'w', encoding='utf-8')
            f.write(res)
            f.close()
            return res
    return wrapper


@read_cache
def get(url):
    return requests.get(url).text


print(get("https://zhuanlan.zhihu.com/p/50076084"))
