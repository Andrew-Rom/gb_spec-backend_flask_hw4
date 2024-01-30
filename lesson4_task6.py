# Задание №6
#   Написать программу, которая считывает список из 10 URL-адресов
#   и одновременно загружает данные с каждого адреса.
#   После загрузки данных нужно записать их в отдельные файлы.
#   Используйте асинхронный подход.

import asyncio
from pathlib import Path


async def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        words = len(f.read().split())
    print(f'{f.name} contents {words} words')


async def main():
    tasks = []
    dir_path = Path('downloaded')
    file_list = [file for file in dir_path.iterdir() if file.is_file()]
    for file in file_list:
        task = asyncio.create_task(read_file(file))
        tasks.append(task)
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
