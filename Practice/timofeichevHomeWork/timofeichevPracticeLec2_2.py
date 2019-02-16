print("Введите 2 числа:")
a = int(input("Введите первое число:"))
b = int(input("Введите второе число:"))

def test(a, b):

    if a>b:
        return("Большее число это:", a)
    if b>a:
        return("Большее число это:", b)
    if a==b:
        return("Введенные числа равны друг другу:",a==b)
    print("Конец")

print (test(a, b))