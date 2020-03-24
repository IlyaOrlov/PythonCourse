c = input('Введите  число: ')
print("Число {}".format(c))
b = 0
while b < len(c):
    for i in range(len(c)):
        b+=1
        print('{} цифра равна  {}'.format(b,c[i]))