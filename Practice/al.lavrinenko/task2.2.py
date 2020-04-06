def greater_number(x, y):
    if x > y:
        return x
    else:
        return y


a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))
c = greater_number(a, b)

print(c)  # for testing purpose
