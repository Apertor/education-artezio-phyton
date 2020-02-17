"""hometask 8.3"""
# Напишите функцию, которая получает два аргумента
#   1)путь к файлу изображения jpeg на компьютере (строка);
#   2)имя целевого файла (строка)
#   отправляет файл HTTP POST запросом на https://postman-echo.com/post .
#   В ответе будет получен файл изображения jpeg,
#   в виде octet-stream, который нужно раскодировать и
#   сохранить на компьютере под целевым именем, переданным в аргументе.
#   Функция должна вернуть размер сохраненного файла.

import requests

PATH = r"d:\Work\el_motory.jpg"


def image_send(path, name):
    """ send image to postman-echo.com"""
    url = "https://postman-echo.com/post"
    # headers = {}
    # headers['Content-Type'] = 'multipart/form-data'
    img_file = open(path, 'rb')
    files = {'file': (name, img_file, 'image/jpeg', {'Expires': '10'})}
    response = requests.post(url, files=files)
    return response.text.encode('utf8')


print(image_send(PATH, "cool_image.jpg"))
