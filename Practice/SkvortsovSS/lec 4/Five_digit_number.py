def five_digit_number():
    print("enter a five-digit number")
    a = list(input())
    k=1
    for i in a:
        print(k,"digit is equal to", i)
        k+=1

five_digit_number()