def MaxNum(a, b):
    if a > b:
        print("Max number: ", a)
    elif a < b:
        print("Max number: ", b)
    else:
        print("Please, enter different number")
a = input("Enter number A: ")
b = input("Enter number B: ")
MaxNum(a, b)