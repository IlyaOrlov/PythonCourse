#Задание №1

l = range(1, 101)

def test(l):

    for i in (l):
        if i % 3 == 0:
            i = 'Fizz'

        elif i % 5 == 0:
            i = 'Buzz'

        elif i % 15 == 0:
            i = 'FizzBuzz'
        print(i)
test(l)


#Задание №2

a = int(10819)
b = str(a)
c = 0
for i in (b):
    c += 1
    print('{} цифра равна {}'.format(c, i))






