# Задание №1
#   Написать программу, которая считывает список из 10 URL-адресов
#   и одновременно загружает данные с каждого адреса.
#   После загрузки данных нужно записать их в отдельные файлы.
#   Используйте потоки.

import requests
import threading

urls = ['https://www.google.ru/',
        'https://gb.ru/',
        'https://ya.ru/',
        'https://www.python.org/',
        'https://habr.com/ru/all/',
        'https://developer.mozilla.org/ru/',
        'https://losst.pro/',
        'https://www.rambler.ru/',
        'https://htmlacademy.ru/',
        'https://www.fannydemier.com/']


def download(url):
    response = requests.get(url)
    filename = 'downloaded/threading_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
    with open(filename, "w", encoding='utf-8') as f:
        f.write(response.text)


threads = []

for url in urls:
    thread = threading.Thread(target=download, args=[url])
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
