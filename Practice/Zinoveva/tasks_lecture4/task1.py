def printNumber():
    for number in range(1,101):
        if (number % 15) is 0:
            print ("FizzBuzz")
        elif (number % 3) is 0:
            print ("Fizz")
        elif (number % 5) is 0:
            print ("Buzz")
        else:
            print (number)


if __name__ == '__main__':
    printNumber()

