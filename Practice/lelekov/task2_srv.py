def sravni_prnt(a, b):
    if a == b:
        print('Числа равны')
    elif a > b:
        print (a)
    else:
        print (b)

def sravni_rtrn(a, b):
    if a == b:
        print('Числа равны')
        return None
    elif a > b:
        return a
    else:
        return b


x = int(input('Введите число 1 ',))
y = int(input('Введите число 2 ',))
print('Введите номер функции:')
print('1- Функция, принимающую два числа и выводящую на экран большее из двух')
print('2- Функция, принимающую два числа и возвращающую большее из двух')
vib = int(input('Введите номер ',))
if vib == 2:
   z = sravni_rtrn(x, y)
   print (z)
elif vib == 1:
     sravni_prnt(x, y)
else:
    print('Выбор не верен :)')
