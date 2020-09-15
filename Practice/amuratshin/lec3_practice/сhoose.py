#программа должна загадывать число, пользователь должен угадывать
import random


def choose():
    number = random.randint(1, 10)
    while True:
        guess = int(input("Введите целое число: "))
        if guess == number:
            print("Поздравляю, вы угадали")
            break
        elif guess < number:
            print("Нет, загаданное число немного больше этого")
        else:
            print("Нет, загаданное число немного меньше этого")
    print("Завершено")


choose()
