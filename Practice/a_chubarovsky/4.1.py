lst1 = [x for x in range(1, 101)]

for i in range(len(lst1)):
    if lst1[i] % 15 == 0:
        print('FizzBuzz')
    else:
        if lst1[i] % 5 == 0:
            print('Buzz')
        else:
            if lst1[i] % 3 == 0:
                print('Fizz')
            else:
                print(lst1[i])
