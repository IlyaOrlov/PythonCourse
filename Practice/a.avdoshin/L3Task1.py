# 22.11 - [ИО]:  Проверено (ОК).
for i in range(1, 101):#gg
    if i%15 == 0:
        print('FizzBuzz')
    elif i%3 == 0:
        print('Fizz')
    elif i%5 == 0:
        print('Buzz')
    else:
        print(i)