import time
import random
import threading


# Первый вариант:
def f(a, b, c):
    # do something
    pass


th = threading.Thread(name='th', target=f, args=(1, 2), kwargs={'c': 3})
# name - имя потока. Ни на что не влияет, но может быть полезно при отладке.
# target - точка входа (любой callable object, функция, связанный метод класса).
# args - позиционные аргументы.
# kwargs - именованные аргументы.


# Второй вариант:
class MyThread(threading.Thread):
    def __init__(self, a, b, c):
        threading.Thread.__init__(self)
        self.a = a
        self.b = b
        self.c = c


def run(self):
    # do something, using self.a, self.b, self.c
    pass
# Результат практически тот же самый, но в новом потоке будет запущен метод run.


th1 = MyThread(1, 2, 3)


def compute(number):
    # вычисления
    print('Start №{}'.format(number))
    sleeping = random.randint(1, 5)
    time.sleep(sleeping)
    print('End №{}'.format(number, sleeping))


start = time.perf_counter()

for i in range(5):
    compute(i)
print('Time sec: {}'.format(int(time.perf_counter() - start)))

