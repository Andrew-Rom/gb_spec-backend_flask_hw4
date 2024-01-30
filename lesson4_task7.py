# Задание №7
#   Напишите программу на Python, которая будет находить
#   сумму элементов массива из 1000000 целых чисел.
#       Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
#   Массив должен быть заполнен случайными целыми числами от 1 до 100.
#   При решении задачи нужно использовать многопоточность, многопроцессорность и асинхронность.
#   В каждом решении нужно вывести время выполнения вычислений.
import asyncio
import multiprocessing
import random
import threading
import time
from concurrent.futures import ProcessPoolExecutor

base_array = [random.randint(1, 100) for _ in range(1_000_000)]

counter_threading = 0
result_threading = 0


def calc_threading(arr):
    global result_threading, counter_threading
    try:
        while counter_threading < len(arr):
            result_threading += arr[counter_threading]
            counter_threading += 1
    except IndexError:
        pass


def calc_multiprocessing(arr):
    return sum(arr)


counter_asyncio = 0
result_asyncio = 0


async def async_calc(arr):
    global result_asyncio, counter_asyncio
    while counter_asyncio < len(arr):
        result_asyncio += arr[counter_asyncio]
        counter_asyncio += 1


async def main():
    tasks = [asyncio.create_task(async_calc(base_array)) for _ in range(5)]
    await asyncio.gather(*tasks)


if __name__ == '__main__':

    start_time = time.time()
    result = 0
    for i in range(len(base_array)):
        result += base_array[i]
    print(f"Sync calculation {time.time() - start_time:.2f} seconds (result: {result})\n")

    threads = []
    start_time = time.time()
    for i in range(5):
        t = threading.Thread(target=calc_threading, args=[base_array])
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print(f"Calculation via threading "
          f"{time.time() - start_time:>10.2f} "
          f"seconds (result: {result_threading})")

    start_time = time.time()

    procs = multiprocessing.cpu_count()
    operation_per_cpu = int(len(base_array) / procs)
    print(f"CPU: {procs}")

    with ProcessPoolExecutor(max_workers=procs) as executor:
        futures = [executor.submit(calc_multiprocessing, base_array[i:i + operation_per_cpu]) for i in
                   range(0, len(base_array), operation_per_cpu)]
        mid_results = [future.result() for future in futures]
        result_multiprocessing = sum(mid_results)

    print(f"Calculation via multiprocessing "
          f"{time.time() - start_time:.2f} seconds "
          f"(result: {result_multiprocessing:>5})")

    start_time = time.time()
    asyncio.run(main())
    print(f"Calculation via asyncio "
          f"{time.time() - start_time:>12.2f} seconds "
          f"(result: {result_asyncio})")
