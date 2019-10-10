import itertools


# функция 1
def chain_total(list1, list2, list3):
    total_list = list(itertools.chain(list1, list2, list3))
    return total_list


# проверка функции 1
print(chain_total([1, 2, 3], [4, 5], [6, 7]))


# функция 2
def len_arr(list1):
    new_list = list(itertools.filterfalse(lambda x: len(x) < 5, list1))
    return new_list


# проверка функции 2
print(len_arr(['hello', 'i', 'write', 'cool', 'code']))


# функция 3
def combination(str1, r):
    new_list = list(itertools.combinations(str1, r))
    return new_list


# проверка функции 3
print(combination('password', 4))