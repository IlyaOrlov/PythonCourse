def printNumber(number):
    for char in enumerate(number):
        print ('{} number is {}'.format(char[0] + 1, char[1]) )


if __name__ == '__main__':
    print("input a five digit number:")
    number = input()
    if not number.isdigit():
        print ("input only numbers")
    elif len(number) != 5:
        print ("input only five symbols")
    else:
        printNumber(number)

