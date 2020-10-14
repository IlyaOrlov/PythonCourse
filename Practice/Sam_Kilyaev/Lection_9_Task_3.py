import threading
import random


def private_data(data):
    data.number = random.randint(1, 100)
    print(f'My name is {threading.current_thread().name} and I have this data: {data.__dict__}')


if __name__ == '__main__':
    p = []
    local_data = threading.local()
    for i in range(9):
        pk = threading.Thread(target=private_data, args=(local_data,))
        pk.start()
        p.append(pk)
    for i in p:
        i.join()
