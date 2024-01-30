# Задание №4
#   Создать программу, которая будет производить подсчет
#   количества слов в каждом файле в указанной директории и
#   выводить результаты в консоль.
#   Используйте потоки.

import threading
from pathlib import Path

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        words = len(f.read().split())
    print(f'{f.name} contents {words} words')

threads = []
dir_path = Path('downloaded')
file_list = [file for file in dir_path.iterdir() if file.is_file()]

for file in file_list:
    thread = threading.Thread(target=read_file, args=[file])
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()