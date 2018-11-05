# 04.11 - [ИО]:  Проверено (OK).
#for Python 3.6
#task 2

def number_reader(x):
    if x.isdigit() and len(x) == 5:
        for i in range(5):
            print("{} цифра равна {}".format(i+1, x[i]))
    else:
        print("Это не пятизначное число")


if __name__ == '__main__':
    number_reader(input("Введите пятизначное число:\n"))
