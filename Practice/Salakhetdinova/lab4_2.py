number = input("enter a five-digit number: ")

def reoutput(n):
    count = 1
    for i in n:
        print(f"{count} number is {i}")
        count = count + 1

reoutput(number)