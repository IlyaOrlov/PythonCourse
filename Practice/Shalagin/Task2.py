number = input("Введите пятизначное число: ")
while len(number) != 5 and int(number):
    number = input("Введите пятизначное число: ")
while number:
    print(number[0])
    number = number[1:]

