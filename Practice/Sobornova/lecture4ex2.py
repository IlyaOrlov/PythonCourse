numbers = input("Введите пятизначное число: ")
a = 0
if numbers.isdigit() and len(numbers) == 5:
    for number in str(numbers):
        a += 1
        print(str(a) + " цифра равна " + number)
else:
    print("Это не число или это число не пятизначное.")
