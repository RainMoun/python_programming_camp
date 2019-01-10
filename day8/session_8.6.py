from urllib.request import urlopen


def index(url):
    def get_content():
        return urlopen(url).read()
    return get_content


get_content_from_url = index('http://www.sohu.com')
print(get_content_from_url().decode('utf-8'))