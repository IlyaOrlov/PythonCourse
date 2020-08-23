# Составить программу,которая будет считывать введённое пятизначное число.
# После чего,каждую цифру этого числа необходимо вывести в новой строке:

def number():
    arr = list(str(int(input("Enter number of 5 digits: "))))
    array = []
    k = 0
    for i in arr:
        k += 1
        array.append(f"{k} цифра равна {i}")
    return "\n".join(array)


print(number())





