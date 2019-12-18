s = input("Введите 5 чисел:")
a = 1
while not s.isdigit() or len(s) != 5:
    s = input("Вы ввели не 5 чисел! Попробуйте еще!")
else:
    for i in s:
        print(a, 'число равно', i)
        a = a + 1

