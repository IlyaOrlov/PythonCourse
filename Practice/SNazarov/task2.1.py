def numbers(a, b):
    if a > b:
        print("First number is bigger: " + str(a))
    else:
        print("Second number is bigger: " + str(b))

print("Enter two nubmers, please!")
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

numbers(first, second)
