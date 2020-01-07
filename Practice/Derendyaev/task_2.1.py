a = int(input("Введите первое число:"))
b = int(input("Введите второе число:"))
def fmax():
    if a > b:
        max = a
    else:
        max = b
    print("Наибольшее число", max)
c = fmax()