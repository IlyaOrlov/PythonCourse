num = input('Enter 5-digit number: ')

if num.isdigit():

    if len(num) == 5:
        i = 0

        for x in num:
            i += 1
            print('The {} number is {}'.format(i, x))
    else:
        print('The number is not 5-digit.')
else:
    print('Some characters are not digits.')
