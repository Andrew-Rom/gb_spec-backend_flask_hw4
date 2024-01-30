# Задание №5
#   Создать программу, которая будет производить подсчет
#   количества слов в каждом файле в указанной директории и
#   выводить результаты в консоль.
#   Используйте процессы.

from multiprocessing import Process
from pathlib import Path

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        words = len(f.read().split())
    print(f'{f.name} contents {words} words')

processes = []
dir_path = Path('downloaded')
file_list = [file for file in dir_path.iterdir() if file.is_file()]

if __name__ == '__main__':
    for file in file_list:
        process = Process(target=read_file, args=(file,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()