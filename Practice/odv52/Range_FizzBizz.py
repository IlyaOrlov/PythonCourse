x = range(1, 100)

def check(x):
    for i in x:
        if i % 3 == 0:
            i = 'Fizz'
        elif i % 5 == 0:
            i = 'Buzz'
        elif i % 15 == 0:
            i = 'FizzBuzz'
        print(i)
check(x)