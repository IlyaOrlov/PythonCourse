a = input("Введите текст: ")
b = input('Введите символ для подсчета: ')


def count_symbol(a, b):
    i = 0
    j = 0
    while i < len(a):
        if b == a[i]:
            j += 1
        i += 1
    return j


print(count_symbol(a, b))


