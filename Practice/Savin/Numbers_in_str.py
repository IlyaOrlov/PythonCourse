number = input('Введите число: ')
print(f'Число: {number}')
for i in range(len(number)):
    print(f"{i + 1} цифра равна {number[i]}")