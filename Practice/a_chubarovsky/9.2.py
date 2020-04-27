import multiprocessing as mp
import time
import itertools as it


sum_list = [0, '', []]


def my_sum(data):
    proc_name = mp.current_process().name
    for arg in data:
        if type(arg) == int:
            sum_list[0] += arg
            print(f"{proc_name} processed value {arg}")
        if type(arg) == str:
            sum_list[1] += ' ' + arg
            print(f"{proc_name} processed value {arg}")
        if type(arg) == list:
            sum_list[2] += list(it.chain(arg))
            print(f"{proc_name} processed value {arg}")
        time.sleep(1)
    if proc_name == 'Process-1':
        print(f"{proc_name} finished with result: {sum_list[0]}")
    if proc_name == 'Process-2':
        print(f"{proc_name} finished with result: {sum_list[1]}")
    if proc_name == 'Process-3':
        print(f"{proc_name} finished with result: {sum_list[2]}")


if __name__ == '__main__':
    start = time.time()
    data = [1, 2, 3, 'Hello', 'World', [1, 2, 3, 9], [4, 5, 6, 10], 5, 11, 'Something', [4, 8, 4], 'How are you?', 100,
            100, [1, 1, 1, 1, 1]]
    num_proc = 3
    processes = [mp.Process(target=my_sum, args=(data,)) for i in range(num_proc)]
    for proc in processes:
        proc.start()
    for proc in processes:
        proc.join()
    print("Lead time = {:.2f} sec.".format(time.time() - start))
