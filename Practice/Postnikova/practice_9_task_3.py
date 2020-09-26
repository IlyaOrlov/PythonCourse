import threading
import random

#Task 3

thread_local = threading.local()

def save_private_data():
    my_list = ['threads', 'processes', 'Queue', 'GIL', 'mutex', 'Pipe']
    secret = getattr(thread_local, 'secret', None)
    if secret is None:
        secret = random.choice(my_list)
        thread_local.secret = secret
    print(f"Thread {threading.current_thread().name} knows secret about {secret}")

all_threads = []

for i in range(6):
    thread_local.initialized = True
    thr = threading.Thread(target=save_private_data, args=( ))
    thr.start()
    all_threads.append(thr)

for thr in all_threads:
    thr.join()
    print('Thread {} is joined'.format(thr))