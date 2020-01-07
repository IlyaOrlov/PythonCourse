for x in range(1,100):
    if x % 15 == 0:
        x = "FizzBuzz"
    elif x % 5 == 0:
        x = "Buzz"
    elif x % 3 == 0:
        x = "Fizz"
    print(x)