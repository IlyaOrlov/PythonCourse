# Task-1 Написать реализацию встроенной функции len: функция принимает список, возвращает его длину. (3 балла)

# word = input('\nEnter word: ')
# def func(word):
#     a = 0
#     for b in word:
#         a += 1
#     return a
# print(func(word))
#___________________________________________________


# Task-2 Написать реализацию функции reversed: функция принимает список, возвращает его же, располагая элементы
# в обратном порядке. (3 балла)

# def func():
#     num1 = input('Enter number: ')
#     num = list(num1)
#     x = 0
#     while x < len(num) / 2:
#         num[x], num[len(num) - x - 1] = num[len(num) - x - 1], num[x]
#         x += 1
#     return num
# print(func())
#___________________________________________________


# Task-5 Написать функцию count_symbol: считает сколько раз символ встречается в строке. (3 балла)

# word = input('Enter word: ')
# search = input('Enter search letter: ')
# def CountSymbol(w, s):
#     a = 0
#     for b in w:
#         if b == s:
#             a += 1
#     return a
# print(CountSymbol(word, search))