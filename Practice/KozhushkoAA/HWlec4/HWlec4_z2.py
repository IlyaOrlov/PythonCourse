# Задание №2
a = input("Enter five-digit number - ")

def Recursion(a):
    if len(a) == 5 and a.isdigit():
        n = 0
        for i in a:
            n += 1
            print('{} цифра равна {}'.format(n, i))
    else:
        print('Not a five-digit number!')
        a = input("Enter five-digit number again - ")
        Recursion(a)


Recursion(a)


