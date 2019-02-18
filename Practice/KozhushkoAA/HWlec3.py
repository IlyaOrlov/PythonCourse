a = 'exit'
i = input('Введите целое число - ')
while i != a:
    if i.isdigit():
        print(int(i)**2)
        break
    else:
        print("Введено не число, либо число не целое")
        break
print("OUT")