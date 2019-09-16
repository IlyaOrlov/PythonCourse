for i in range(1, 101):
    if i % 3 != 0 and i%5 != 0:
        print(i, end=" ")
    elif i % 3 == 0 and i%5 != 0:
        print("Fizz", end=" ")
    elif i % 3 != 0 and i % 5 == 0:
        print("Buzz", end=" ")
    else:
        print("FizzBuzz", end=" ")