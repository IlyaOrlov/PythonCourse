
"""
This module prints integer numbers from 'a' to 'b'/
If number is multiple to 3 module prints 'Fizz',
if number is multiple to 5 module prints 'Buzz',
and if number is multiple to 15 module prints 'FizzBuzz'.
"""

a = int(input('Enter the first (minimal) number: a = '))
b = int(input('Enter the second (maximal) number: b = '))
for k in range(a,b):
    if k % 15 == 0:
        print('FizzBuzz')
    elif k % 5 == 0:
        print('Buzz')
    elif k % 3 == 0:
        print('Fizz')
    else:
        print(k)