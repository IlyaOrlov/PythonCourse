import threading


class myThread(threading.Thread):

   def __init__(self, data):
       threading.Thread.__init__(self)
       self.data = data

   def run(self):
       only_my_data(self)   # our target


def only_my_data(self):
   print(f'I am {threading.current_thread().name}. I have this data: {self.data}')


if __name__ == "__main__":
    big_data = [1, 2, "three", [4, 4], "five", 6, "seven"]
    threads = []
    for i in range(len(big_data)):
        thr = myThread(big_data[i])
        thr.start()        # call run()
        threads.append(thr)

    for thr in threads:
        thr.join()
        
# or
'''
import threading
import random


def only_my_data(data):
    data.number = random.randint(1, 1000)
    print(f'I am {threading.current_thread().name}. I have this data: {data.__dict__}')


if __name__ == '__main__':
    threads = []
    local_data = threading.local()

    for i in range(7):
        t = threading.Thread(target=only_my_data, args=(local_data,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

'''
