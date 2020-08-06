def numbers(a, b):
    if a > b:
        print(f"First number is bigger: {a}")
    else:
        print(f"Second number is bigger: {b}")

print("Enter two nubmers, please!")
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

numbers(first, second)
