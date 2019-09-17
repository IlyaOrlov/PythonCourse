def compare_and_return(x,y):
    if x>y:
        return x
    else:
        return y

# If You want to input variables from keyboard
# def compare_and_return(x, y):
#     if float(x) > float(y):  # change str type to float
#         return x
#     else:
#         return y
# x = input('enter first number: x = ')
# y = input('enter second number: y = ')
# z = compare_and_return(x,y)
# print('The largest number is '+str(z))

# for testing
print('The largest number is', compare_and_return(2,100))

