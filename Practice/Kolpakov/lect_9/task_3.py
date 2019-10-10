import threading
import random


def private_func():
    private_data = random.randint(0,100)
    print(f'Приватные данные: {private_data} {threading.current_thread().name}')


for i in range(5):
    my_thread = threading.Thread(target=private_func)
    my_thread.start()
    my_thread.join()