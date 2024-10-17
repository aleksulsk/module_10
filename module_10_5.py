from datetime import datetime
from multiprocessing import pool

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)



filenames = [f'./file {number}.txt' for number in range(1, 5)]

start_time = datetime.now()

for filename in filenames:
    read_info(filename)

end_time = datetime.now()
time_res = end_time - start_time
print(f"{time_res} - линейный")
# Линейный вызов
if __name__ == '__main__':
    start_time_multiprocessing = datetime.now()
    with pool.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    end_time_multiprocessing = datetime.now()
    time_res_multiprocessing = end_time_multiprocessing - start_time_multiprocessing
    print(f"{time_res_multiprocessing} - мультипроцессный")
# Многопроцессный

