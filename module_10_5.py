from multiprocessing import Pool
from time import time

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        for readline in file:
            all_data.append(readline)

filenames = [f'./file {number}.txt' for number in range(1, 5)]


if __name__ == '__main__':
    # Линейная обработка файлов
    start_time = time()
    for i in filenames:
        results1 = read_info(i)
    end_time = time()
    print(end_time - start_time)

    # Многопроцессорная обработка файлов
    start_time = time()
    with Pool() as pool:
        results2 = pool.map(read_info, filenames)
    end_time = time()
    print(end_time - start_time)