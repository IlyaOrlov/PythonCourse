c = (input('Введите  число: '))
print("Число {}".format(c))
for i in range(len(c)):
    print('{} цифра равна  {}'.format(i+1, c[i]))