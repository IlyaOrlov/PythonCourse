def number_to_numbers(num):
    num = str(num)
    count = 1
    for i in num:
        print(count, '\tцифра равна ', i)
        count += 1
    print('\n')


x = 55624
b = 5548962134
number_to_numbers(x)
number_to_numbers(b)
