num = input("Введите число: ")
while not num.isdigit():
    num = input("Ошибка. Введите число: ")
print("Число:", num)
t = 1
for i in num:
    print("{} цифра равна {} ".format(t, i))
    t += 1