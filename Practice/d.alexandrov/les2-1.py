print("Sequence from 1 to 100")
for i in range(1,100):
    if i % 15 == 0:
        print("FizzBuzz")
        continue
    elif i % 3 == 0:
        print("Fizz")
        continue
    elif i % 5 == 0:
        print("Buzz")
        continue
    else:
        print(i)
