number = input("Please enter a five-digit number: ")
for x in range(len(number)):
    print("{} figure is equal {}".format(x + 1, number[x]))
