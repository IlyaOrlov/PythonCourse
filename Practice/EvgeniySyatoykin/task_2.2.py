def numbers(a, b):
    if a > b:
        return a
    else:
        return b

print("Enter two nubmers, please!")
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
result = numbers(first, second)
print(f"This number is bigger: {result}")

numbers(first, second)
