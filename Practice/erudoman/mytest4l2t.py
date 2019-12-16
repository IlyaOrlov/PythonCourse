s = input("Введите 5 чисел:")
while not s.isdigit():
    s = input("Вы ввели не 5 чисел! Попробуйте еще!")
else:
    while len(s) != 5:
        s = input("Вы ввели не 5 чисел! Попробуйте еще!")
    else:
        for i in s:
            print(i)
