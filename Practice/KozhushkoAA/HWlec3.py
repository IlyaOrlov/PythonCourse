a = 'exit'
i = input('Введите число - ')

while i != a:
    if i.isdigit():
        print(int(i)**2)
    else:
        print("Введено не число, либо число не целое или отрицательное")
    i = input('Снова введите число - ')
print(i)


