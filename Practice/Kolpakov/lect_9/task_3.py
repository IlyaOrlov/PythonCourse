import threading
import random


def private_func():
    try:
        print(private_data)
    except Exception:
        print('No data')
    private_data = random.randint(0,100)
    print(f'Приватные данные: {private_data} {threading.current_thread().name}')


threads = []
for i in range(5):
    my_thread = threading.Thread(target=private_func)
    my_thread.start()
    threads.append(my_thread)

for j in threads:
    j.join()