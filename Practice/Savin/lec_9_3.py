import threading

class MyThread(threading.Thread):

    def __init__(self, func, kwargs):
        threading.Thread.__init__(self)
        self.func = func
        self._kwargs = kwargs

    def run(self):
        self.func(**self._kwargs)


def player(fname, lname, age):
    thread = threading.current_thread().name
    print(f'Name Thread: {thread}\ndata:\nfull name: {fname} {lname}, age: {age}\n')

data1 = {'fname': 'Jhon', 'lname': 'Terry', 'age': 25}
data2 = {'fname': 'Frank', 'lname': 'Lampard', 'age': 30}
data3 = {'fname': 'Johe', 'lname': 'Cole', 'age': 35}

t1 = MyThread(func=player, kwargs=data1)
t2 = MyThread(func=player, kwargs=data2)
t3 = MyThread(func=player, kwargs=data3)

threads = [t1, t2, t3]

for t in threads:
    t.start()
for t in threads:
    t.join()
