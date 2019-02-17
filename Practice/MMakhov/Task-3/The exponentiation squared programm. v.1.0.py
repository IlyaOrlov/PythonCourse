print("The exponentiation squared programm. v.1.0")
print()

a = (input("Please, enter an integer: "))
if a.isdigit():
    print((a), 'sqr2 =', int(a)**2)
else:
    print("Your number not integer! Enter only integer!")

b = (input("You want EXIT the programm? Yes/No"))
while b != "Yes":
    b = (input("Enter integer ('Yes' for exit programm): "))
    if b.isdigit():
        print((b), 'sqr2 =',int(b)**2)
    elif b == "Yes":
        print()
    else:
        print("Only integer!")
print('Programm closed! Thank you for using!')
