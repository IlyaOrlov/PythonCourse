def fizz_buzz(border):
    for i in range(1, border + 1):
        yield 'FizzBuzz' if not i % 15 else 'Fizz' if not i % 3 else 'Buzz' if not i % 5 else i


for item in fizz_buzz(100):
    print(item)
