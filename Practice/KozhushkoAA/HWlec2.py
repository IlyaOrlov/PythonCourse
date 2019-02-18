#Задание 1:
def max_num(a, b):
    if a == b:
        print('Числа равны')
    else:
        print(max(a, b))
a = int(input('Введите ЦЕЛОЕ ЧИСЛО a - '))
b = int(input('Введите ЦЕЛОЕ ЧИСЛО b - '))
max_num(a, b)


#Задание 2:
a = int(input('Введите ЦЕЛОЕ ЧИСЛО a - '))
b = int(input('Введите ЦЕЛОЕ ЧИСЛО b - '))
def max_num(a, b):
    if a == b:
        return('Числа равны')
    else:
        return(max(a, b))
#либо
#x = max_num(a, b)
#print(x)
print(max_num(a, b))


#Задание 1 (вариант 2):
def max_num(a, b):
    if a > b:
        print(a)
    elif b == a:
        print('Числа равны')
    else:
        print(b)
a = int(input('Введите ЦЕЛОЕ ЧИСЛО a - '))
b = int(input('Введите ЦЕЛОЕ ЧИСЛО b - '))
max_num(a, b)


#Задание 2 (вариант 2):
a = int(input('Введите ЦЕЛОЕ ЧИСЛО a - '))
b = int(input('Введите ЦЕЛОЕ ЧИСЛО b - '))
def max_num(a, b):
    if a == b:
        return('Числа равны')
    else:
        return(max(a, b))
#либо
#x = max_num(a, b)
#print(x)
print(max_num(a, b))