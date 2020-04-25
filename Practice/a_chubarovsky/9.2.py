from multiprocessing import Process, Queue, current_process
import time
import itertools as it


def my_sum_int(q, data):
    sum = 0
    for element in data:
        q.put(element)
        if type(element) == int:
            sum += element
            print(f"{current_process().name} processed values {element}")
    print(f"{current_process().name} finished with result = {sum}.")


def my_sum_str(q, data):
    sum = ''
    for element in data:
        q.put(element)
        if type(element) == str:
            sum += ' ' + element
            print(f"{current_process().name} processed values {element}")
    print(f"{current_process().name} finished with result = {sum}.")


def my_sum_lst(q, data):
    sum = []
    for element in data:
        q.put(element)
        if type(element) == list:
            sum += list(it.chain(element))
            print(f"{current_process().name} processed values {element}")
    print(f"{current_process().name} finished with result = {sum}.")


if __name__ == '__main__':
    start = time.time()
    q = Queue()
    data = [1, 2, 3, 'Hello', 'World', [1, 2, 3, 9], [4, 5, 6, 10], 5, 11, 'Something', [4, 8, 4], 'How are you?', 100,
            100, [1, 1, 1, 1, 1]]
    p1 = Process(target=my_sum_int, args=(q, data))
    p2 = Process(target=my_sum_str, args=(q, data))
    p3 = Process(target=my_sum_lst, args=(q, data))
    p1.start()
    p2.start()
    p3.start()
    q.close()
    p1.join()
    p2.join()
    p3.join()
    print("Lead time = {:.2f} sec.".format(time.time() - start))
