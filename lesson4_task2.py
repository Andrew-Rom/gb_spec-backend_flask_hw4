# Задание №2
#   Написать программу, которая считывает список из 10 URL-адресов
#   и одновременно загружает данные с каждого адреса.
#   После загрузки данных нужно записать их в отдельные файлы.
#   Используйте процессы.

from multiprocessing import Process
import requests

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
    filename = 'downloaded/multiprocessing_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
    with open(filename, "w", encoding='utf-8') as f:
        f.write(response.text)


processes = []

if __name__ == '__main__':
    for url in urls:
        process = Process(target=download, args=(url,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
