def MaxReturnNum(a, b):
    if a > b:
        return a
    elif a < b:
        return b
    else:
        print("Please, enter different number")
a = input("Enter number A: ")
b = input("Enter number B: ")
MaxReturnNum(a, b)