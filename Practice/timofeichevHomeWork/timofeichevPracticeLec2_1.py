print("Введите 2 числа:")
a = int(input("Введите первое число:"))
b = int(input("Введите второе число:"))

def test(a, b):
    if a > b:
        print("Большее число это:", a)
    elif b > a:
        print("Большее число это:", b)
    else:
        print("Введенные числа равны друг другу:")
    print("Конец")
test(a, b)
