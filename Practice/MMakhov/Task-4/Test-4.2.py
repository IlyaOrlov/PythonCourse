X = input('Please, enter five-digit number: ')
if len(X) == 5:
    Z = 0
    for i in X:
        Z += 1
        print('{} цифра равна {}'.format(Z, i))
else:
    print ('Enter only five-digit number!!!')