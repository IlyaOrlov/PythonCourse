from itertools import combinations


def comb(x):
    """Выдает на строку все возможные комбинации."""
    data = list(combinations(x, 4))
    return data


print(comb('password'))
#
#
#
#
from itertools import chain


def return_array(one, two, three):
    """Принимает три массива и возвращает один массив."""
    new_list = list(chain(one, two, three))
    return new_list


print(return_array([1, 2, 3], [4, 5], [6, 7]))
#
#
#
#
from itertools import filterfalse


def work_with_array(array):
    """Принимает массив и вовзращает массив из элементов
    , у которых длина не меньше пяти."""
    new_array = list(filterfalse(lambda x: len(x) < 5, array))
    return new_array


print(work_with_array(['hello', 'i', 'write', 'cool', 'code']))
