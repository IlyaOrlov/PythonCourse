num = input("Введите пятизначное число: ")
while len(num) != 5 or not num.isdigit():
    num = input("Ошибка. Введите пятизначное число: ")
print("Число:", num)
t = 1
for i in num:
    print("{} число равно {} ".format(t, i))
    t += 1