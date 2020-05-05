import threading
import copy


class DataThread(threading.Thread):
    def __init__(self, data):
        threading.Thread.__init__(self)
        self.__data = copy.deepcopy(data)

    def run(self):
        print_data(self.__data)


def print_data(data):
    print(f'{threading.current_thread().name} contains:', data)


test_lst = [[x*y for x in range(1, 31)] for y in range(1, 8)]
threads = []
for lst in test_lst:
    threads.append(DataThread(lst))
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
