# Num 3
import time
import random


class TimeManager:

    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        print(f'Run time code: ({self.end_time - self.start_time}) second')


with TimeManager():
    for i in range(random.randint(0, 800000)):
        print(i)

# Num4
# Функция должна принимать три массива ([1, 2, 3], [4, 5], [6, 7]), а вернуть
# лишь один массив ([1, 2, 3, 4, 5, 6, 7])
from itertools import chain

mass = ([1, 2, 3], [4, 5], [6, 7])
my_mass = list(chain.from_iterable(mass))
print(my_mass)

# Функция принимает массив (['hello', 'i', 'write', 'cool', 'code']) и возвращает
# массив из элементов, у которых длина не меньше пяти (['hello', 'write'])
from itertools import filterfalse

mass_1 = ['hello', 'i', 'write', 'cool', 'code']


def five(x):
    return len(x) < 5


my_mass_1 = list(filterfalse(five, mass_1))
print(my_mass_1)

# Функция выдает на строку 'password' все возможные комбинации вида
# ([('p', 'a', 's', 's'), ('p', 'a', 's', 'w'), ('p', 'a', 's', 'o'), ...)
from itertools import combinations


st = 'password'

comb = list(combinations(st, 4))
print(comb)
