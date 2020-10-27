fives_number = input("Write your number: ")


def reoutput(number):
    count = 1
    for i in number:
        print(f"{count} number is {i}")
        count = count + 1


reoutput(fives_number)
