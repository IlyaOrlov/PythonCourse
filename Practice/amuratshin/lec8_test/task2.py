# 1. Написать реализацию встроенной функции len: функция принимает
# список, возвращает его длину. (3 балла)


def lst_length(lst):
    length = 0
    for i in lst:
        length += 1
    return length


f_list = ['1', '3', '4']
print(lst_length(f_list))       # 3


# 2. Написать реализацию функции reversed: функция принимает список,
# возвращает его же, располагая элементы в обратном порядке. (3 балла)


def lst_reverse(lst):
    new_list = lst[::-1]
    return new_list


print(lst_reverse(f_list))      # ['4', '3', '1']


# 4. Написать функцию to_title: принимает строку, ищет пробелы, первые
# буквы после них и после начала строки делает заглавными. (3 балла)


def to_title(str):
    return ' '.join(s[:1].upper() + s[1:] for s in str.split(' '))


f_str = "How can mirrors be real if our eyes aren't real"
print(to_title(f_str))      # Azamat Muratshin Radikovich


# 5. Написать функцию count_symbol: считает сколько раз символ
# встречается в строке. (3 балла)


def count_symbol(string, symbol):
    count = 0
    for letter in string:
        if symbol == letter:
            count += 1
    return count


string1 = "Hi, Elvis, I am here!"
print(count_symbol(string1, 'i'))   # 2


