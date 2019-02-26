x = 0
for x in range(1,100):
    if x % 3 == 0 and x % 5 != 0:
        x = "Fizz"
        print(x)
    elif x % 5 == 0 and x % 3 != 0:
        x = "Buzz"
        print(x)
    elif x % 15 == 0:
        x = "FizzBuzz"
        print(x)
    else:
        print(x)
print("exiting")