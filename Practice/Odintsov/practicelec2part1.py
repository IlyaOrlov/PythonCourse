print('Enter two numbers')
x = int(input("first number:"))
y = int(input("second number:"))

def greater_number(x, y):
    if x > y:
        print('greater number is', x)
    elif x < y:
        print('greater number is', y)
    elif x == y:
        print("first number equally second number")

print (greater_number(x, y))


