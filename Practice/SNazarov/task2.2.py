def numbers(a, b):
    if a > b:
        return a
    else:
        return b

print("Enter two nubmers, please!")
first = input("Enter first number: ")
second = input("Enter second number: ")
result = numbers(first, second)
print("This number is bigger: " + result)

numbers(int(first), int(second))
