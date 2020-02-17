"""hometask 8.1"""
# Напишите функцию, которая возвращает
# размер HTML документа по адресу https://google.com.
# Т.е. нужно получить страницу и
# вернуть ее размер (количество символов).

import requests

URL1 = 'https://www.google.com/'


def html_size(url):
    """return content-length by document url"""
    r = requests.get(url, stream=True, headers={'Accept-Encoding': None})
    return r.headers['Content-length']


print(html_size(URL1))
