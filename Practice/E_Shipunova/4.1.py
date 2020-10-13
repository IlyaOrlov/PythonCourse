def fizz_buzz():
    for i in range(1, 101):  # for 1-100
        if i % 15 == 0:      # the first condition, else have to be: 'if i % 3 == 0 and i % 15 != 0:  ...'
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


fizz_buzz()
