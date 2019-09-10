def compare_and_return(x,y):
    if x>y:
        return x
    else:
        return y

# for testing
x = input('enter first number: x = ')
y = input('enter second number: y = ')
z = compare_and_return(x,y)
print('The largest number is '+str(z))