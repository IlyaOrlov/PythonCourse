i = 1
while i < 101:
    print(i)
    i += 1
    if i % 15 == 0:
        print('FizzBuzz')
        i += 1
    if i % 3 == 0:
        print('Fizz')
        i += 1
    if i % 5 == 0:
        print('Buzz')
        i += 1
        if i % 3 == 0:
            print('Fizz')
            i += 1
