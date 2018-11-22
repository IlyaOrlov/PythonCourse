def get_number():
    print("Please enter 5-digit number")
    x = input("Number: ")
    while not x.isdigit() or len(x) != 5:
        print("You entered non-digit string or it's lenght is less than 5.")
        x = input("Number: ")
    return x


num = get_number()
for i in range(0, 5):
    print(i, " digit is ", num[i])
