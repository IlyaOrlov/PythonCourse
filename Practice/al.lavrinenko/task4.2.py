while True:
    number = input("Enter 5-digit number: ")
    if number.isdigit() == 0:
        print("Error: only numbers should be here, enter again")
    elif len(number) != 5:
        print("Error: this number is not 5-digit, enter again")
    elif number[0] == '0':
        print("Error: the 1st digit can't be zero, enter again")
    else:
        break

for i in range(len(number)):
    print("The {} digit is {}".format(i+1, number[i]))
