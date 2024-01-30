# Задание №3
#   Написать программу, которая считывает список из 10 URL-адресов
#   и одновременно загружает данные с каждого адреса.
#   После загрузки данных нужно записать их в отдельные файлы.
#   Используйте асинхронный подход.

import asyncio

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


async def download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text = await response.text()
            filename = 'downloaded/asyncio_' + url.replace('https://','').replace('.', '_').replace('/', '') + '.html'
            with open(filename, "w", encoding='utf-8') as f:
                f.write(text)

async def main():
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(download(url))
        tasks.append(task)
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
