lst = list(range(1, 101))

i=0
for i in range(len(lst)):
    if lst[i]%15 == 0:
        lst[i] = "FizzBuzz"
    elif lst[i]%3 == 0:
        lst[i] = "Fizz"
    elif lst[i]%5 == 0:
        lst[i] = "Buzz"

    print(lst)

