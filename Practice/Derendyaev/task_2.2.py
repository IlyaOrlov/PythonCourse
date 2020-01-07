a = int(input("Введите первое число:"))
b = int(input("Введите второе число:"))
def fmax(a, b):
    if a > b:
        max = a
    else:
        max = b
    return max
c = fmax(a, b)
print("Наибольшее из двух", c)