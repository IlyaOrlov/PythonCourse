def multiple_numbers():
    """выводит числа от 1 до 100 кратные 3 и 5"""
    for i in range(0, 101):
        val3 = i % 3
        val5 = i % 5
        if val3 == 0 and val5 == 0:
            print('FizzBuzz', i)
        elif val3 == 0:
            print('Fizz', i)
        elif val5 == 0:
            print('Buzz', i)


multiple_numbers()