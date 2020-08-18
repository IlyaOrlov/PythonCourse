from functools import reduce

fizzbuzz = lambda n: 'FizzBuzz' if n % 15 == 0 else None
fizz = lambda n: 'Fizz' if n % 3 == 0 else None
buzz = lambda n: 'Buzz' if n % 5 == 0 else None
fizz_andor_maybenot_buzz = lambda n: fizzbuzz(n) or fizz(n) or buzz(n) or str(n)
print(reduce(lambda m,n: m+'\n'+n, map(fizz_andor_maybenot_buzz, range(1, 101))))