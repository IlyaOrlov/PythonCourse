import re


# Напишите программу, которая выводит на экран числа от 1 до 100 При этом вместо чисел,
# кратных трем, программа должна выводить слово Fizz а вместо чисел, кратных пяти
# слово Buzz Если число кратно пятнадцати, то программа должна выводить слово FizzBuzz

def fizz_buzz():
    for i in range(1, 101):
        if i % 15 == 0:
            print('FizzBuzz')
        elif i % 5 == 0:
            print('Buzz')
        elif i % 3 == 0:
            print('Fizz')
        else:
            print(i)


fizz_buzz()


# Составить программу, которая будет считывать введённое пятизначное число После чего,
# каждую цифру этого числа необходимо вывести в новой строке

def number_line_by_line(number):
    count = 1
    for i in number:
        print(f'{count} number is {i}')
        count += 1


your_number = input('Input your number: ')

number_line_by_line(your_number)


# Реализовать алгоритм сортировки выбором. Алгоритм состоит из следующих шагов
# 1 найти наименьший элемент в массиве
# 2 поменять местами его и первый элемент в массиве
# 3 найти следующий наименьший элемент в массиве
# 4 и поменять местами его и второй элемент массива
# 5 продолжать это пока весь массив не будет отсортирован

def arr_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]


array = [19, 15, 27, 8, 0, 21]

arr_sort(array)
print(array)


# Реализовать функциональность, которая бы “сворачивала и разворачивала“ символы
# табуляции в файле или строке То есть, передается на вход файл или строка, необходимо
# заменить все символы табуляции на четыре пробела, либо же заменить все комбинации из
# четырех символов пробела на символ табуляции

def tabulator(string, tab_to_space=True):
    if tab_to_space == True:
        new_string = re.sub('\t', '    ', string)
    else:
        new_string = re.sub('    ', '\t', string)

    return new_string


print(tabulator('Hello\tworld'))
print(tabulator('Hello    world', False))


# Интерполировать некие шаблоны в строке Есть строка с определенного вида
# форматированием необходимо заменить в этой строке все вхождения шаблонов на их
# значение из словаря

def substitution(string):
    dictionary = {'плохое': 'хорошее', 'сомнительный': 'надежный'}
    for key, value in dictionary.items():
        string = string.replace(key, value)
    print(string)

str = 'Сейчас плохое время для заключения сделки. Вы сомнительный партнер.'

substitution(str)

# Есть список списков ( Каждый внутренний список это строка матрицы
# Необходимо реализовать функцию, которая удаляет столбец, который содержит заданную
# цифру

def correcting_matrix(matrix, number):
    for i in matrix:
        j = 0
        while j < len(i):
            if i[j] == number:
                delete_column(matrix, j)
                j -= 1
            j += 1
    return matrix


def delete_column(matrix, j):
    for i in range(len(matrix)):
        matrix[i].pop(j)


exaple1 = [[1, 2, 3], [4, 5, 6, ], [7, 8, 9]]
exaple2 = [[1, 2, 3], [4, 5, 6, ], [7, 8, 9]]
exaple3 = [[1, 2, 2, 0], [4, 5, 6, 1], [7, 8, 9, 2]]

print(correcting_matrix(exaple1, 5))
print(correcting_matrix(exaple2, 1))
print(correcting_matrix(exaple3, 2))
