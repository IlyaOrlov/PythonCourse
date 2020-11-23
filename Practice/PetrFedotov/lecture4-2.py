input_num = input("enter a five-digit number: ")

def line(number):
    count = 1
    for i in number:
        print(f"{count} number is {i}")
        count += 1

line(input_num)