x=1
while x<=100:
    if x%3==0:
        print('Fizz')

    if x%5==0:
        print('Buzz')

    if x%15==0:
        print('FizzBuzz')

    elif x%3!=0 and x%5!=0 and x%15!=0:
        print(x)
    x += 1